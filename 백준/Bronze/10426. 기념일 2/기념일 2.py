# 기념일2
import datetime

s, a = input().rstrip().split()
y, m, d = s.split("-")

start = datetime.date(int(y), int(m), int(d))
add = datetime.timedelta(days=int(a)-1)

print(start + add)