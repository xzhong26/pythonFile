#!/user/bin/python
# coding=utf-8
import csv
from avg5pre2 import classavg5pre2

ts_codes = {}
with open('源数据20200701-20211028 - 副本.csv', mode='r') as f:
    reader = csv.reader(f, delimiter=',')
    for n, row in enumerate(reader):
        if not n:
            continue
        index, ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount = row
        if ts_code not in ts_codes:
            ts_codes[ts_code] = list()
        ts_codes[ts_code].append((index, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount))
    classavg5pre2().avg5pre2(ts_codes)
f.close()