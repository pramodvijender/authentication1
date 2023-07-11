#!/usr/bin/env python
import time

import requests

from concurrent.futures import ThreadPoolExecutor

urls = ['https://wrap.perpetual.com.au']*30

def get_url(url):
    return requests.get(url).status_code

i = 1
while i <25:
    with ThreadPoolExecutor(max_workers=30) as pool:
        print(list(pool.map(get_url,urls)))
        #time.sleep()
    i = i+1

