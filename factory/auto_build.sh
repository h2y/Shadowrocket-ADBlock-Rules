#!/bin/bash

Path=/root/Shadowrocket-ADBlock-Rules
cd $Path

git fetch --all
git reset --hard origin/master

cd factory
python3 ad.py
python3 gfwlist.py
python3 build_confs.py
cd ..

git add .
git commit -m "Nightly build" -m "已合并最新的去广告规则及 GFWList"
git push
