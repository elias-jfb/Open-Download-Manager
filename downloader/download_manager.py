from threading import Thread
from tkinter import messagebox
from utils.logger import get_logger
from config.settings import NUM_CHUNKS_DEFAULT
import requests

class DownloadManager:
    def __init__(self, url, num_chunks=NUM_CHUNKS_DEFAULT, download_list=None, download_file_name="downloaded_file"):
        self.url = url
        self.num_chunks = num_chunks
        self.download_list = download_list
        self.download_file_name = download_file_name
        self.logger = get_logger(__name__)

    def download_file(self):
        response = requests.head(self.url)
        filesize = int(response.headers['Content-Length'])
        chunk_size = filesize // self.num_chunks
        threads = []

        with open(self.download_file_name, 'wb') as f:
            f.truncate(filesize)

        if self.download_list:
            self.download_list.add_download(self.download_file_name, "Started", "0%", "-", f"{filesize} bytes")

        for i in range(self.num_chunks):
            start = i * chunk_size
            end = start + chunk_size - 1 if i < self.num_chunks - 1 else filesize - 1
            thread = Thread(target=self.download_chunk, args=(self.url, start, end, self.download_file_name, i))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        messagebox.showinfo("Download Complete", "Your file has been downloaded successfully!")

    def download_chunk(self, url, start, end, filename, chunk_index):
        headers = {'Range': f'bytes={start}-{end}'}
        response = requests.get(url, headers=headers, stream=True)
        with open(filename, "r+b") as f:
            f.seek(start)
            f.write(response.content)
        if self.download_list:
            progress_percentage = int((end / start) * 100) if start != 0 else 0
            self.download_list.update_download(self.download_file_name, "Downloading", f"{progress_percentage}%", "Calculating", "-")
