#!/user/bin/python27
# coding=utf-8
import csv
# import pandas as pd

f = open("file/updown.csv", "w", encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["ts_code", "index", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount", "tab"])

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
        # print(key, ts_codes[key])
        tsk = ts_codes[key][::-1]
        # print("---------------------++++++++++++++++---------------------")
        tab = 0
        preMin = 0
        for n, row in enumerate(tsk):

            if tab == 1:
                closePre = float(tsk[n-1][5])     # 上一天
                closeCur = float(tsk[n][5])     # 当前
                m = 0
                if closePre >= closeCur:
                    m = closeCur
                else:
                    m = closePre
                if m <= preMin:
                    tab = 1
                    preMin = m
                    csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
                    # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                else:
                    tab = 0
                    preMin = 0
                    print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                    # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
            else:
                if n >= 9:
                    #   取值10个数
                    # close = float(tsk[n-9][5])
                    # close1 = float(tsk[n-8][5])
                    # close2 = float(tsk[n-7][5])
                    # close3 = float(tsk[n-6][5])
                    # close4 = float(tsk[n-5][5])
                    # close5 = float(tsk[n-4][5])
                    # close6 = float(tsk[n-3][5])
                    # close7 = float(tsk[n-2][5])
                    # close8 = float(tsk[n-1][5])
                    # close9 = float(tsk[n][5])

                    #   取值10个数
                    closes = []
                    i = 9
                    while i >= 0:
                        closes.append(float(tsk[n - i][5]))
                        i-=1
                    #   获取9个数 为10值之差得
                    cMins = []
                    for ix,j in enumerate(closes):
                        print(ix, j)
                        if ix + 1 < len(closes):
                            if closes[ix] <= closes[ix+1]:
                                cMins.append(closes[ix])
                            else:
                                cMins.append(closes[ix+1])

                    if cMins[0] <= cMins[1] <= cMins[2] <= cMins[3] <= cMins[4] >= cMins[5] >= cMins[6] >= cMins[7] >= cMins[8]:
                        tab = 1
                        preMin = cMins[8]
                        print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                        # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
                    else:
                        tab = 0
                        preMin = 0
                        print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                        # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
                else:
                    tab = 0
                    preMin = 0
                    print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                    # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
        # break
f.close()