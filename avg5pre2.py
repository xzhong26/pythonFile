#!/user/bin/python27
# coding=utf-8
import csv


class classavg5pre2():
    def avg5pre2(self, ts_codes):
        f = open("file/avg5pre2.csv", "w", encoding='utf-8', newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow(["ts_code", "index", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount", "avg5close", "avg5pre2", "avg10"])

        for key in ts_codes:
            # print("---------------------++++++++++++++++---------------------")
            for n, row in enumerate(ts_codes[key]):
                ll = []
                kk = []
                ll10 = []

                if (n + 9) < len(ts_codes[key]):
                    ll.append(float(ts_codes[key][n][5]))
                    ll.append(float(ts_codes[key][n + 1][5]))
                    ll.append(float(ts_codes[key][n + 2][5]))
                    ll.append(float(ts_codes[key][n + 3][5]))
                    ll.append(float(ts_codes[key][n + 4][5]))

                    ll10.append(float(ts_codes[key][n][5]))
                    ll10.append(float(ts_codes[key][n + 1][5]))
                    ll10.append(float(ts_codes[key][n + 2][5]))
                    ll10.append(float(ts_codes[key][n + 3][5]))
                    ll10.append(float(ts_codes[key][n + 4][5]))
                    ll10.append(float(ts_codes[key][n + 5][5]))
                    ll10.append(float(ts_codes[key][n + 6][5]))
                    ll10.append(float(ts_codes[key][n + 7][5]))
                    ll10.append(float(ts_codes[key][n + 8][5]))
                    ll10.append(float(ts_codes[key][n + 9][5]))

                    dayPre = 2  # 错峰天数
                    kk.append(float(ts_codes[key][n + dayPre][5]))
                    kk.append(float(ts_codes[key][n + 1 + dayPre][5]))
                    kk.append(float(ts_codes[key][n + 2 + dayPre][5]))
                    if (n + 4 + dayPre) >= len(ts_codes[key]):
                        pass
                    else:
                        kk.append(float(ts_codes[key][n + 3 + dayPre][5]))
                        kk.append(float(ts_codes[key][n + 4 + dayPre][5]))
                    avg = (sum(ll) / (len(ll)))

                    avg10 = (sum(ll10) / (len(ll10)))
                    max10 = max(ll10)

                    avgC = (sum(kk) / (len(kk)))
                    if (n + 4 + dayPre) >= len(ts_codes[key]):
                        pass
                    if len(kk) == 5:
                        csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], round(avg, 3), round(avgC, 3), round(avg10, 3)])
                    else:
                        csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], round(avg, 3), "aaaaa", round(avg10, 3)])
                else:
                    csv_writer.writerow([key, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], "xxxxx", "yyyyyy"])
        f.close()
