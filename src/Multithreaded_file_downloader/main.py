import threading
import logging
import os
from .file_downloader import download_file
from .logger import setup_logger

# logging configuration setup
setup_logger()
# download directory path
DOWNLOAD_DIR="data/downloads"
# Main function
def main():
    # all urls with file names
    urls = [
        ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", "file1.pdf"),
        ("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt", "file2.txt"),
        ("https://raw.githubusercontent.com/datasets/population/master/data/population.csv", "file3.csv"),
        ("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt", "file4.txt"),
        ("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt", "file5.txt"),
        ("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt", "file6.txt"),
        ("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/raft-medium-directories.txt", "file7.txt"),
        ("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", "file8.csv"),
        ("https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt", "file9.txt"),
        ("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt", "file10.txt"),
    ]
    # list to keep track of threads
    threads = []
    
    for idx, (url, filename) in enumerate(urls):
        # full path where files will be downloaded
        file_path = os.path.join(DOWNLOAD_DIR, filename)
        # creating a new thread for each file
        thread = threading.Thread(target=download_file, args=(url, file_path, idx))
        # adding thread to the thread list
        threads.append(thread)
        # starting thread
        thread.start()
        

    # Wait for all threads
    for thread in threads:
        thread.join()

    logging.info("All threads completed.")

if __name__ == "__main__":
    main()
