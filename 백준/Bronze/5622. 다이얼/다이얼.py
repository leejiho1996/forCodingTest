# 다이얼

dial = {"ABC":2, "DEF":3, "GHI":4, "JKL":5, "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9}

word = input()
total = 0

for i in word:
    for j in dial.keys():
        if i in j:
            total += dial[j]+1

print(total)
