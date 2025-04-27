import os
import sys
from bs4 import BeautifulSoup as bs
from requests import Session
from termcolor import colored
from .utils import escape, unitSize

s = Session()

def downloadVideos(link: str, offset: int = 0):
    """
    Downloads videos from the given MIT OpenCourseWare link.
    Args:
        link (str): The URL of the MIT OpenCourse video resources.
        offset (int): The offset for the video list (default: 0).
    """
    vids, folder = crawl_link(link, offset)
    if not vids:
        print("No videos found.")
        return
    
    print("Downloading videos from:", link)
    print("Total Videos:", len(vids))

    for vid in vids:
        vid_next = vid.fetchNextSiblings(attrs={"class": "resource-list-item-details"})
        vid_name = escape(vid_next[0].getText(" ", True))
        vid_path = os.path.join(folder, vid_name + ".mp4")

        file_exists = os.path.exists(vid_path)
        file_size = os.path.getsize(vid_path) if file_exists else None

        try:
            reqResource = s.get(vid.attrs.get("href"), headers=({'Range': 'bytes=%d-' % file_size} if file_exists else {}), stream=True)

        except Exception as err:
            print("Error:", err)

        else:
            total_length = reqResource.headers.get('content-length')
            os.makedirs(folder, exist_ok=True)
            print("Downloading:", vid_name)

            with open(vid_path, "ab" if file_exists else "wb") as f:
                if total_length is None:
                    resResource = reqResource.content
                    f.write(resResource)

                else:
                    dl = file_size if file_exists else 0
                    total_length = int(total_length) + int(dl)

                    download_with_progress(reqResource, f, dl, total_length)

            print("\nDownload complete:", vid_name, "File saved at:", vid_path)



def crawl_link(link: str, offset: int = 0):
    """
    Crawls the given link to extract video resources.
    Args:
        link (str): The URL of the MIT OpenCourse video resources.
        offset (int): The offset for the video list (default: 0).
    Returns:
        tuple: A tuple containing the list of video resources and the folder name.
    """

    request = s.get(link)
    response = request.content

    tree = bs(response, "html.parser")
    title = tree.find("title").getText(" ", True)

    folder = os.path.join("MIT OpenCourse Videos", "-".join(title.split("|")[1:-1]).strip())
    vids = tree.find_all("a", {"class": "resource-thumbnail"})[offset:]
    return vids, folder


def download_with_progress(reqResource, f, downloaded, total_length):
    """
    Downloads the resource with progress indication.
    Args:
        reqResource: The request resource to download.
        f: The file object to write to.
        downloaded: The current download size.
        total_length: The total length of the resource.
    """
    for data in reqResource.iter_content(chunk_size=4096):
        downloaded += len(data)
        f.write(data)

        done = int(50 * downloaded / total_length)
        prog = colored('━', "green")
        rem = colored('━', "dark_grey")

        sys.stdout.write("\r[%s%s] %s of %s" % (prog * done, rem * (50-done), f"{done * 2}%", unitSize(total_length)))
        sys.stdout.flush()