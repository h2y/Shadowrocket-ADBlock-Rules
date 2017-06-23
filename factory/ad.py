# -*- coding: utf-8 -*-

import time
import sys
import requests
import re


rules_url = [
    'https://easylist-downloads.adblockplus.org/easylistchina.txt',  # EasyList China
    'https://github.com/cjx82630/cjxlist/raw/master/cjxlist.txt'     # EasyList Lite
]

# contain both domains and ips
domains = []


for rule_url in rules_url:
    print('loading... ' + rule_url)

    # get rule text
    success = False
    try_times = 0
    while try_times < 5 and not success:
        r = requests.get(rule_url)
        if r.status_code != 200:
            time.sleep(1)
            try_times = try_times + 1
        else:
            success = True
            break

    if not success:
        sys.exit('error in request %s\n\treturn code: %d' % (rule_url, r.status_code) )

    rule = r.text

    # parse html
    reg_ret = re.findall(r'\|\|([\w\.]+)\^?\n', rule)
    for ret in reg_ret:
        domains.append(ret)

    print('done.')


# write in files

domains.sort()

file_ad = open('resultant/ad.list', 'w', encoding='utf-8')

file_ad.write('# ad rules refresh time: ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n')

last = ''
for item in domains:
    if last == item:
        continue
    file_ad.write(item + '\n')
    last = item
