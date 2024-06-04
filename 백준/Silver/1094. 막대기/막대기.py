# 막대기
import sys

target = int(input())

sticks = [64]

while True:
    if sum(sticks) > target:
        half = sticks[-1] // 2
        sticks[-1] = half
        if sum(sticks) >= target:
            pass
        else:
            sticks.append(half)
        
    if sum(sticks) == target:
        print(len(sticks))
        break
