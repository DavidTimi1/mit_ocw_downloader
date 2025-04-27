from setuptools import setup, find_packages

setup(
    name='mit_ocw_downloader',
    version='0.1.0',
    author='David Uwagbale',
    author_email='duwagbale07@gmail.com',
    description='A package for downloading MIT OpenCourseWare lecture videos.',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'mit_ocw_downloader=mit_ocw_downloader.__main__:main',
        ],
    },
)