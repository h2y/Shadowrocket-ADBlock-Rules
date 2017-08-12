# -*- coding: utf-8 -*-

import time
import sys
import requests
import re


rules_url = [
    # EasyList China
    #'https://easylist-downloads.adblockplus.org/easylistchina.txt',
    # EasyList + China
    'https://easylist-downloads.adblockplus.org/easylistchina+easylist.txt',
    # 乘风 广告过滤规则
    'https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/ABP-FX.txt'
]

# contain both domains and ips
domains = []


for rule_url in rules_url:
    print('loading... ' + rule_url)

    # get rule text
    success = False
    try_times = 0
    r = None
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
    rule = rule.split('\n')
    for row in rule:
        if not row.startswith('||') and not row.startswith('|http'):
            continue

        # del prefix
        row = re.sub(r'^\|(\||https?:\/\/)', '', row)
        # del suffix
        row = row.rstrip('/^ ')

        if re.search(r'[\$\^:\*]', row):
            continue
        if row.count('/'):
            continue

        if not re.match(r'\w+(\.\w+)+$', row):
            continue

        # match
        domains.append(row)

    print('done.')


# write into files

domains.sort()

file_ad = sys.stdout
try:
    if sys.version_info.major == 3:
        file_ad = open('resultant/ad.list', 'w', encoding='utf-8')
    else:
        file_ad = open('resultant/ad.list', 'w')
except:
    pass

file_ad.write('# adblock rules refresh time: ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n')

last = ''
for item in domains:
    if last == item:
        continue
    file_ad.write(item + '\n')
    last = item
