#!/usr/bin/env python3

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def download(url):
    driver = webdriver.Chrome()
    urlp = "https://doi.org/" + url
    print(urlp)
    driver.get(urlp)
    time.sleep(1000)
for line in sys.stdin:
    download(line.rstrip())
