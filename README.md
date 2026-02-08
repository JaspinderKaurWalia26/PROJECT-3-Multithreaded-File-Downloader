# Multithreaded File Downloader

## Project Overview
This project is a Multithreaded File Downloader built using Python.
It downloads multiple files from the internet concurrently using threads, making the download process faster and more efficient compared to sequential downloading.

---
## What Does This Project Do?
- Downloads multiple files from given URLs
- Uses multithreading to perform downloads concurrently
- Tracks progress for each download
- Logs download status and errors using the logging module
- Handles failures gracefully without stopping the entire program

---

## Why Was Multithreading Used?
Multithreading was used in this project because downloading files is an I/O-bound task that mostly involves waiting for data from the internet. If files are downloaded one by one, the program has to wait for each download to finish, which increases the total execution time. By using multithreading, multiple files can be downloaded at the same time, which reduces the overall time taken and prevents a slow download from blocking the others.


---

##  Technologies Used
- Python 3
- threading module
- os
- logging module
- time module
- urllib.request 

---

## Project Structure

```
data/
│
├── downloads/      # All downloaded files here
│ ├── file1.pdf
│ ├── file2.txt
│ ├── file3.csv
│ ├── file4.txt
│ ├── file5.txt
│ ├── file6.txt
│ ├── file7.txt
│ ├── file8.csv
│ ├── file9.txt
│ └── file10.txt
│
logs/
│ └── app.log   # Logging file for program execution
│
src/
│ └── Multithreaded_file_downloader/
│ ├──__init__.py  # Allows importing files from this folder as a package
│ ├── file_downloader.py #file downloading logic 
│ ├── logger.py # Logging setup
│ └── main.py   # Program entry point
│
├── README.md  # Project documentation
```

## How to Run
### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/PROJECT-3-Multithreaded-File-Downloader.git
cd PROJECT-3-Multithreaded-File-Downloader
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
This project does not require any external dependencies.  
All required modules are part of Python’s standard library.
```
### 5. Run the program
```
python -m src.Multithreaded_file_downloader.main
```
### 6. Check outputs

- Downloaded files: data/downloads/

- Logs: logs/app.log



