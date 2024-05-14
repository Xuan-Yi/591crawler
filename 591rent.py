import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from tqdm import tqdm
from datetime import datetime
from line_notify import line_notify

URL = "https://rent.591.com.tw/?section=5,7,1,12&searchtype=1&kind=3&multiNotice=not_cover,all_sex,boy&showMore=1&rentprice=10000,15000&order=posttime&orderType=desc&shType=best_house"
house_prefix = "https://rent.591.com.tw/home/"
line_token = ""
max_pages = 2
time_sleep = 60

def show_current_time():
    nowtime = datetime.now()
    current_time = nowtime.strftime("%H:%M:%S")
    print(current_time)
    return current_time

def wait_time(time_sleep):
    print()
    for t in tqdm(range(int(time_sleep)), desc = f"Sleeping {time_sleep} minutes ..."):
        time.sleep(60)
    print()

def get_url_from_id(id_set, prefix):
    url_set = set()
    for id_str in id_set:
        url_set.add(prefix + id_str)
    return url_set

service = Service('./chromedriver')
options = Options()
options.headless = True
house_sets = set()

while True:
    browser = webdriver.Chrome(service = service, options = options)
    try:
        browser.get(URL)
        time.sleep(2)
        current_time = show_current_time()
        new_sets = set()
        for i in range(max_pages):
            soup = BeautifulSoup(browser.page_source, "lxml")
            for item in soup.find_all("section", attrs={"class": "vue-list-rent-item"}):
                link = item.find("a")
                new_sets.add(link.attrs["href"].split("-")[-1].split(".")[0])
            browser.find_element(by=By.CLASS_NAME, value="pageNext").click()
            time.sleep(random.random() * 2 + 1)
        if new_sets != house_sets:
            print("Found new house!")
            diff_set = new_sets - house_sets
            url_set = get_url_from_id(diff_set, prefix = house_prefix)
            print(url_set)
            line_notify(f"Found new house!", token = line_token)
            for url in url_set:
                status_code = line_notify(url, token = line_token)
                if status_code != 200:
                    print("Line notify status code:", status_code)
                    break
                time.sleep(1)
        house_sets = new_sets
        browser.close()
        wait_time(time_sleep)
    except Exception as e:
        browser.close()
        current_time = show_current_time()
        print(f"Browser Error! [{current_time}]: {e}")
        line_notify(f"Browser Error! [{current_time}]: {e}", token = line_token)
        break