#!/user/bin/python27
# coding=utf-8
import csv

f = open("file/arrange.csv", "w", encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["ts_code", "index", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount", "arrange"])
ts_codes = {}
with open('源数据20200701-20211028 - 副本.csv', mode='r') as f:
    reader = csv.reader(f, delimiter=',')  # dialect=csv.excel_tab?
    for n, row in enumerate(reader):
        if not n:
            continue
        index, ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount = row
        if ts_code not in ts_codes:
            ts_codes[ts_code] = list()
        ts_codes[ts_code].append((index, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount))

    for key in ts_codes:
        
        tsk = ts_codes[key][::-1]
        # print(key, tsk)
        # print("---------------------++++++++++++++++---------------------")
        count = 0
        for n, row in enumerate(tsk):
            # print(n, row)
            highs = []
            lows = []
            closes = []
            opens = []
            # if n < len(tsk):
            if n > 1:
                close = float(tsk[n][5])
                close1 = float(tsk[n + 1][5])
                if count >= 5:
                    day =  count
                else:
                    day = 4

                
                # 校验收盘价 上一天收盘和当天收盘 差值大于4%
                if abs((float(close) - float(close1)) / float(close)) > 0.04:
                    high0 = float(tsk[n][3]) # 阳柱当天的最高
                    low0 = float(tsk[n][4]) # 阳柱当天的最低
                    close0 = float(tsk[n][5])  # 当天的收盘close
                    open0 = float(tsk[n][2])  # 当天的开盘
                    i = -count
                    while i > day:
                        i += 1
                        if n - i < len(tsk):
                            # high = float(tsk[n + i][3])
                            # highs.append(high)
                            # low = float(tsk[n + i][4])
                            # lows.append(low)
                            close = float(tsk[n + i][5])
                            closes.append(close)
                            open = float(tsk[n + i][2])
                            opens.append(open)
                    status = False
                    # print(key, row[1], close, min(hh), max(llo), min(clo) )
                    if max(closes) < high0:
                        if low0 < min(opens):
                            if min(closes) > low0:
                                status = True
                        else:
                            count = 0
                    if status:           
                        count += 1
                    else:
                        count = 0
                else:
                    count = 0
                # csv_writer.writerow([key, row[1], row[2], row[3],row[4],row[5],count])
            else:
                pass
                # csv_writer.writerow([key, row[1], row[2], row[3],row[4],row[5],count])
            if count >= 5:
                print("sssssssssssssssssssss", count)
            print(key, row[1], row[2], row[3],row[4],row[5],count)
        # break
f.close()
