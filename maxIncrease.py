#!/user/bin/python27
# coding=utf-8
import csv
import time

f = open("file/maxIncrease.csv", "w", encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["ts_code", "index", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount", "increase", "max"])
ts_codes = {}


stataTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
print("time begin", stataTime)
with open('源数据20200701-20211028 - 副本.csv', mode='r') as f:
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
        # print(key, ts_codes[key])
        # print("---------------------++++++++++++++++---------------------")
        for n, row in enumerate(ts_codes[key]):
            #--------
            increase = 0
            if (n + 1) < len(ts_codes[key]):
                increase = float(ts_codes[key][n][5]) - float(ts_codes[key][n+1][5])
            else:
                increase = 0
            ics = []

            maxRound = 0
            if len(ts_codes[key]) - n - 1 > 29:
                maxRound = 29
            else:
                maxRound = len(ts_codes[key]) - n - 1

            num = 0
            if (n + num) <= len(ts_codes[key]):
                while num < maxRound:
                    ic = float(ts_codes[key][n + num][5]) - float(ts_codes[key][n + 1 + num][5])
                    num += 1
                    ics.append(ic)
                maxIc = max(ics, default=0)
                csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], increase, maxIc])
f.close()
endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
print("time end", endTime)