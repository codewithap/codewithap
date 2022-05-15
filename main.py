from ast import Try
import requests
import time
import os
print("\n\n")

RED = '\033[41m'
GREEN = '\033[32m'
WHITE = '\033[37m'
blue="\033[34m"
RESET_ALL = '\033[0m'
bold='\033[01m'

def request(i,urls):
    response = []
    for url in urls:
        while True:
            if url == "":
                break
            try:
                r = requests.get(url,timeout=10)
                break
            except:
                print("failed!")
                pass
        response.append([r,url])
        a = ""
        if i == 1:
            a = "request"
        if i > 1:
            a = "requests"
        if url == "":
            break
        if r.status_code == 200:
            print(f"{blue+url}{RESET_ALL} | {GREEN}{r}{RESET_ALL}")
        if r.status_code != 200:
            print(f"{WHITE}{bold}{RED} failed {RESET_ALL}| {blue+url+RESET_ALL} | {r}")
        time.sleep(1)
    return response

i = 1
while True:
    while True:
        try:
            urls = (requests.get("https://raw.githubusercontent.com/codewithap/codewithap/main/workingLinks.txt").text).split("\n")
            print(urls)
            break
        except:
            print("ERROR")
            time.sleep(5)
            pass
    request(i,urls)
    print(RESET_ALL)
    i = i + 1
    time.sleep(600)
 