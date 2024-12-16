#solved.ac
import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    exit()
    
diffi = []
for i in range(n):
    diffi.append(int(input()))

cut = n * 0.15
if cut * 10 % 10 >= 5:
    cut = int(cut) + 1
else:
    cut = int(cut)
    
diffi.sort()
diffi_cut = diffi[cut:n-cut]

total = 0
for i in diffi_cut:
    total += i

total /= len(diffi_cut)
if total * 10 % 10 >= 5:
    total = int(total) + 1
else:
    total = int(total)

print(total)
