#!/user/bin/python27
# coding=utf-8
import csv

# f = open("file/arrange.csv", "w", encoding='utf-8', newline="")
# csv_writer = csv.writer(f)
# csv_writer.writerow(["ts_code", "index", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount", "arrange"])
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

    # for key in ts_codes:
        
    key = "300873.SZ"
    tsk = ts_codes[key][::-1]
    # print(key, tsk)
    # print("---------------------++++++++++++++++---------------------")
    count = 0
    for n, row in enumerate(tsk):
        closes = []
        opens = []
        if n >= 5:
            day = 4 #默认取阳柱后4天
            if count >= 5:
                day =  count
            close = float(tsk[n - day][5]) # 假设阳柱标准
            close1 = float(tsk[n - day - 1][5]) #阳柱的前一天

            # 校验收盘价 上一天收盘和当天收盘 差值大于4%
            if abs((float(close) - float(close1)) / float(close)) > 0.04:
                high0 = float(tsk[n - day][3]) # 阳柱当天的最高
                low0 = float(tsk[n - day][4]) # 阳柱当天的最低
                i = 0 #（0，1，2，3）
                while i < day:
                    close = float(tsk[n - i][5])
                    closes.append(close)
                    open = float(tsk[n - i][2])
                    opens.append(open)
                    i += 1
                print("kkkkkkkkk", n, high0, low0, closes, opens, len(closes), len(opens), max(closes) < high0, low0 < min(opens),min(closes) > low0)
                status = False
                # print(key, row[1], close, min(hh), max(llo), min(clo) )
                if max(closes) < high0:
                    if low0 < min(opens):
                        if min(closes) > low0:
                            status = True
                if status:
                    if count >= 5:
                        count += 1
                    else:           
                        count = 5
                else:
                    count = 0
            else:
                count = 0
            # csv_writer.writerow([key, row[1], row[2], row[3],row[4],row[5],count]）
        
        print(key, tsk[n][1], tsk[n][2], tsk[n][3],tsk[n][4],tsk[n][5],count)
        # break
f.close()
