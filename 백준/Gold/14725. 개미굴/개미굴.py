# 개미굴
import sys
input = sys.stdin.readline

n = int(input())

sett = set()
word_list = []
dic = {}

for i in range(n):
    k = input().split()
    word = "".join(k[1:])
    word_list.append(word)
    dic[word] = k[1:]

word_list.sort()

for i in word_list:
    ant_room = dic[i]
    used = ""
    for j, v in enumerate(ant_room):
        used += v
        if used in sett:
            continue
        sett.add(used)
        print("-"*(j*2), v, sep='')
