#!/user/bin/python27
# coding=utf-8
import csv
# import pandas as pd

f = open("file/xxxx.csv", "w", encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["ts_code", "trade_date", "open", "high", "low", "close", "tabUpDown", "countZL", "Hengpan", "multiResult"])

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
        count = 0 # 整理的输出结果

        avgHp = 0   # 横盘均价
        avgHpMax = 0    # 横盘均价max
        avgFMax = 0 # 非横盘时候取上个横盘价
        record = 0
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
                    # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
                    # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                else:
                    tab = 0
                    preMin = 0
                    # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                    # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
            else:
                if n >= 9:
                    
                    #   取值10个数
                    closes = []
                    i = 9
                    while i >= 0:
                        closes.append(float(tsk[n - i][5]))
                        i-=1
                    #   获取9个数 为10值之差得
                    cMins = []
                    for ix,j in enumerate(closes):
                        # print(ix, j)
                        if ix + 1 < len(closes):
                            if closes[ix] <= closes[ix+1]:
                                cMins.append(closes[ix])
                            else:
                                cMins.append(closes[ix+1])

                    if cMins[0] <= cMins[1] <= cMins[2] <= cMins[3] <= cMins[4] >= cMins[5] >= cMins[6] >= cMins[7] >= cMins[8]:
                        tab = 1
                        preMin = cMins[8]
                        # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                        # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
                    else:
                        tab = 0
                        preMin = 0
                        # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                        # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])
                else:
                    tab = 0
                    preMin = 0
                    # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab)
                    # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], tab])

            # 整理================
            highs = []
            lows = []
            closes = []
            opens = []
            # if n < len(tsk):
            if n > 1:
                close = float(tsk[n][5])
                close1 = float(tsk[n - 1][5])
                if count >= 5:
                    day =  -count
                else:
                    day = -4

                
                # 校验收盘价 上一天收盘和当天收盘 差值大于4%
                if abs((float(close) - float(close1)) / float(close)) > 0.04:
                    high0 = float(tsk[n][3]) # 阳柱当天的最高
                    low0 = float(tsk[n][4]) # 阳柱当天的最低
                    close0 = float(tsk[n][5])  # 当天的收盘close
                    open0 = float(tsk[n][2])  # 当天的开盘
                    i = 1
                    while i > day:
                        i -= 1
                        if n - i < len(tsk):
                            high = float(tsk[n - i][3])
                            highs.append(high)
                            low = float(tsk[n - i][4])
                            lows.append(low)
                            close = float(tsk[n - i][5])
                            closes.append(close)
                            open = float(tsk[n - i][2])
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
                        if count < 5:
                            count = 5
                        else:
                            count += 1
                    else:
                        count = 0
                else:
                    count = 0
            #     csv_writer.writerow([key, row[1], row[2], row[3],row[4],row[5],count])
            # else:
            #     csv_writer.writerow([key, row[1], row[2], row[3],row[4],row[5],count])


            # 横盘 =============
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
                # 校验第一天和第五天的差值小于2%
                if abs((float(close5)/float(close1))-1) > 0.02:
                    status = False
                if abs(close2 / ((close1 + close5)/2)-1) > 0.08 and abs(close3 / ((close1 + close5)/2)-1) > 0.08 and abs(close4 / ((close1 + close5)/2)-1) > 0.08:
                    status = False
                for index, item in enumerate(ll):
                    # 校验每天的价格与均价的百分比
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
                    # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], status, round(avgHpMax, 3), round(avg, 3), "++++++++++++++++")
                else:
                    avgFMax = avgHpMax
                    
                    # csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], status, round(avgHp, 3)])
                    # print(key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], status, round(avgFMax, 3))
            result = False
            if float(row[2]) > 30 and float(row[3]) > 30 and float(row[4]) > 30:
                result = True
            csv_writer.writerow([key, row[1], row[2], row[3],row[4],row[5], tab, count, round(avgHpMax, 3), result])
        # break
f.close()