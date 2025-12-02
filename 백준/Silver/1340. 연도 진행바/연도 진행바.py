# 연도 진행바
import sys
input = sys.stdin.readline

idx = {"January" : 0, "February":31, "March":59, "April":90,
       "May":120, "June":151, "July":181, "August":212, "September":243,
       "October":273, "November":304, "December":334}

Month, DD, YYYY, HHMM = input().rstrip().split()

HH, MM = HHMM.split(":")

Month = idx[Month]
DD = (int(DD[:-1])-1)
HH = int(HH) * 60
MM = int(MM)
YYYY = int(YYYY)

if YYYY % 400 == 0 or (YYYY % 4 == 0 and YYYY % 100 != 0):
    year = 366 * 24 * 60

    if Month >= 59:
        DD += 1

else:
    year = 365 * 24 * 60

Month = Month * 60 * 24
DD = DD * 60 * 24

print((Month + DD + HH + MM) / year * 100)
