import threading
import logging
import os
from .file_downloader import download_file
from .logger import setup_logger


setup_logger()
DOWNLOAD_DIR="data/downloads"
# Main function
def main():
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

    threads = []

    for idx, (url, filename) in enumerate(urls):
        file_path = os.path.join(DOWNLOAD_DIR, filename)
        t = threading.Thread(target=download_file, args=(url, file_path, idx))
        threads.append(t)
        t.start()
        

    # Wait for all threads
    for t in threads:
        t.join()

    logging.info("All threads completed.")

if __name__ == "__main__":
    main()
