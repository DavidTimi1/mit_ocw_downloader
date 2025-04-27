import sys
import argparse
from mit_ocw_downloader.downloader import downloadVideos

def main():
    parser = argparse.ArgumentParser(description="Download MIT OpenCourse videos.")
    parser.add_argument("url", type=str, help="The URL of the MIT OpenCourse video resources.")
    parser.add_argument("--offset", type=int, default=0, help="The offset for the video list (default: 0).")
    # parser.add_argument("--base_dir", type=str, default="videos", help="The base directory where the folder containing all downloaded videos will be stored (default: videos).")
    
    args = parser.parse_args()
    
    downloadVideos(args.url, args.offset)

if __name__ == "__main__":
    main()