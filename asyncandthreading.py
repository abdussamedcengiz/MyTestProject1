import threading
import requests
import time
import asyncio
import aiohttp


def get_data_sync(urls):
    st=time.time()
    json_arry=[]
    for url in urls:
        json_arry.append(requests.get(url).json())
    et=time.time()
    elapsed_time=et-st
    print("execution time:",elapsed_time,"seconds")
    return json_arry



class ThreadingDownloader(threading.Thread):
    json_array=[]



    def __init__(self,url):
        super().__init__()
        self.url=url

    def run(self):
        response=requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array

def get_data_threading(urls):
    st = time.time()
    threads=[]
    for url in urls:
        t=ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    et = time.time()
    elapsed_time = et - st
    print("execution time:", elapsed_time, "seconds")


urls=["https://postman-echo.com/delay/3"]
#get_data_sync(urls)
get_data_threading(urls)