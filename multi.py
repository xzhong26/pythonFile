#!/user/bin/python310
# coding=utf-8
import csv

f = open("file/multi.csv", "w", encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["ts_code", "index", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount", "result"])

with open('源数据20200701-20211028 - 副本.csv', mode='r') as f:
    ts_codes = {}
    reader = csv.reader(f, delimiter=',')  # dialect=csv.excel_tab?
    for n, row in enumerate(reader):
        if not n:
            # Skip header row (n = 0).
            continue
        index, ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount = row
        if ts_code not in ts_codes:
            ts_codes[ts_code] = list()
        ts_codes[ts_code].append((index, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount))

    for key in ts_codes:
        tab = 0
        preMin = 0
        for n, row in enumerate(ts_codes[key]):
            result = False
            if float(row[2]) > 30 and float(row[3]) > 30 and float(row[4]) > 30:
                result = True
            csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], result])
f.close()