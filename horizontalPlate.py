#!/user/bin/python27
# coding=utf-8
import csv

# f = open("file/horizontalPlate.csv", "w", encoding='utf-8', newline="")
# csv_writer = csv.writer(f)
# csv_writer.writerow(["ts_code", "index", "trade_date", "open", "high", "low", "close", "status", "avg5hp"])

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

    # for key in ts_codes:
        # print(key, ts_codes[key])
    key = "300019.SZ"
    avgHp = 0   # 横盘均价
    avgHpMax = 0    # 横盘均价max
    avgFMax = 0 # 非横盘时候取上个横盘价
    record = 0
    # tsk = ts_codes["300174.SZ"][::-1]
    tsk = ts_codes[key][::-1]
    # print("---------------------++++++++++++++++---------------------")
    for n, row in enumerate(tsk):
        ll = []
        status = True
        if n >= 4:
            
            close1 = float(tsk[n][5])
            close2 = float(tsk[n - 1][5])
            close3 = float(tsk[n - 2][5])
            close4 = float(tsk[n - 3][5])
            close5 = float(tsk[n - 4][5])

            ll.extend([close1, close2, close3, close4, close5])
            avg = round(sum(ll) / (len(ll)), 3)
            # print("=====", close1, close2, close3, close4, close5, abs((float(close5)/float(close1))-1), "==+++++==",abs(close2 / ((close1 + close5)/2)-1), abs(close3 / ((close1 + close5)/2)-1), abs(close4 / ((close1 + close5)/2)-1), avg )

            
            # 校验第一天和第五天的差值小于2%
            if abs((float(close5)/float(close1))-1) > 0.02:
                status = False
            if abs(close2 / ((close1 + close5)/2)-1) > 0.08 and abs(close3 / ((close1 + close5)/2)-1) > 0.08 and abs(close4 / ((close1 + close5)/2)-1) > 0.08:
                status = False
            for index, item in enumerate(ll):
                # 校验每天的价格与均价的百分比
                print("check",abs((item/avg)-1), item)
                if (abs((item/avg)-1)) > 0.02:
                    status = False
                    break
            
            if status:
                # 满足条件的横盘
                if avg > avgHpMax:
                    avgHpMax = avg
                else:
                    if record > avg:
                        avgHpMax = record
                # 上一个满足条件的均价记录
                record = avg
                print(key, tsk[n][1], tsk[n][2], tsk[n][3],tsk[n][4],tsk[n][5], status, round(avgHpMax, 3), round(avg, 3), "++++++++++++++++")
            else:
                avgFMax = avgHpMax
                
                # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], status, round(avgHp, 3)])
                print(key, tsk[n][1], tsk[n][2], tsk[n][3],tsk[n][4],tsk[n][5], status, round(avgFMax, 3))
        else:
            # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], "status", "xxxx"])
            print(key, tsk[n][1], tsk[n][2], tsk[n][3],tsk[n][4],tsk[n][5], status, "xxxx")
        # break
f.close()