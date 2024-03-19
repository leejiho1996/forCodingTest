#리모컨
import sys
input = sys.stdin.readline

cur = 100
num = [i for i in range(10)]

target = input().rstrip()
a = int(input())
minn = 500001
last = '50001'
if a > 0:
    for i  in list(map(int,input().split())):
        num.remove(i)


def backtrack(target, word):
    global minn 
    global last

    if len(word) >= 2 and word[0] =='0':
        return
    
    if word and minn >= abs(int(word) - int(target)):
        if minn == abs(int(word) - int(target)):
            last = str(min(int(last), int(word)))
        else:
            last = word
        minn = min(minn, abs(int(word) - int(target)))
        
        # print(word)
        
    if int(target[0]) >= 6:
        if len(word) == len(target) + 1:
            return
    else:
        if len(word) == len(target):
            return
    
    for i in num:
        word += str(i)
        backtrack(target, word)
        word = word[:-1]

backtrack(target, '')

minn = min(minn+len(last), abs(int(target) - cur))

print(minn)
