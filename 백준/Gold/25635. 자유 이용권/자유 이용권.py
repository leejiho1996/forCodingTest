# 자유 이용권
import sys
input = sys.stdin.readline

N = int(input())
tickets = list(map(int,input().split()))
tickets.sort(reverse=True)

total = sum(tickets)

if total - tickets[0] >= tickets[0]:
    print(total)
else:
    print(2 * sum(tickets[1:]) + 1)
        
