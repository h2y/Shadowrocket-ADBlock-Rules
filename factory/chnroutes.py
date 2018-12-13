# -*- coding: utf-8 -*-
# 爬取并生成 China Routes，目前此脚本未启用

import time
import re
import requests
import sys


apnic_ip_url = 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
out_file = 'resultant/chnroutes.list'

chnroutes = []


def fetchHTML(url):
    print("Downloading... " + url)

    success = False
    try_times = 0
    r = None
    while try_times < 5 and not success:
        r = requests.get(url)
        if r.status_code != 200:
            time.sleep(1)
            try_times = try_times + 1
        else:
            success = True
            break

    if not success:
        sys.exit('error in request %s\n\treturn code: %d' % (url, r.status_code) )

    r.encoding = 'utf-8'
    return r.text.split('\n')


# Main

# apnic|CN|ipv4|116.89.240.0|1024|20170616|allocated
searchRe = r'^apnic\|CN\|ipv4\|(.+)\|(\d+)\|\d+\|\w+$'

for ln in fetchHTML(apnic_ip_url):
    reRet = re.match(searchRe, ln)
    if not reRet:
        continue

    print(reRet.group())
