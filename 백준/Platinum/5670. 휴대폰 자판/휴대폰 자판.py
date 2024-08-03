# 휴대폰 자판
import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        dic = {}
        word_list = set()
        for i in range(n):
            word = input().rstrip()
            word_list.add(word)
            for idx, v in enumerate(word):
                if idx == 0:
                    char = word[idx]
                    if char not in dic:
                        dic[char] = []
                    continue

                prev = char
                char += word[idx]

                if char not in dic:
                    dic[char] = []

                if len(dic[prev]) >= 2:
                    continue
                
                if char in dic[prev]:
                    continue
                else:
                    dic[prev].append(char)
        
        total = len(word_list)
        for word in word_list:
            if len(word) == 1:
                continue
        
            char = ""
            for j, v in enumerate(word):
                if j == len(word) - 1:
                    continue
                char += v
                if len(dic[char]) >= 1 and char in word_list:
                    total += 1
                    continue
                if len(dic[char]) > 1:
                    total += 1
                    continue
         
        print(f"{total/len(word_list):.2f}")
        
    except:
        break
