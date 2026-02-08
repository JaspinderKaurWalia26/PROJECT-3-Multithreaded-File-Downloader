import threading
import logging
import os
import urllib.request

# dictionary to track download progress
progress = {}    
# thread safety lock
lock = threading.Lock()    

# Function to download file
def download_file(url, filename, thread_id):
    try:
        #logs when a thread starts downloading
        with lock:
            logging.info(f"Thread {thread_id} STARTED downloading {os.path.basename(filename)}")
            progress[thread_id] = 0
        # function to update and calculate progress
        def reporthook(block_num, block_size, total_size):
            if total_size > 0:
                percent = min(100, (block_num * block_size) / total_size * 100)
                with lock:
                    progress[thread_id] = percent
        # downloading the file and tracking progress using reporthook function
        urllib.request.urlretrieve(url, filename, reporthook)
        # updating after completion of download
        with lock:
            progress[thread_id] = 100
            logging.info(f"Thread {thread_id} FINISHED downloading {os.path.basename(filename)}")

    except Exception as e:
        with lock:
            logging.error(f"Thread {thread_id} FAILED downloading {os.path.basename(filename)}. Error: {e}")
