# MIT OpenCourse Downloader

This project is a Python package designed to download lecture videos from MIT OpenCourseWare. It provides a command-line interface for users to easily download videos from specified course URLs.

## Features

- Download lecture videos from MIT OpenCourseWare.
- Supports resuming downloads if dowanloads were stopped.
- Displays download progress in the terminal.

## Installation

To install the package, clone the repository and install the required dependencies:

```bash
git clone https://github.com/davidtimi1/mit_ocw_downloader.git
cd mit_ocw_downloader
pip install -r requirements.txt
```

## Usage

You can run the package from the command line. Use the following command to download videos from a specific course URL:

```bash
python -m mit_ocw_downloader <course_url> [--offset <offset_index>]
```

Replace `<course_url>` with the URL of the course's lecture videos you wish to download. For example:

```bash
python -m mit_ocw_downloader "https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecture-videos/"
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.