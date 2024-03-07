# N과 M 백트래킹

a, b = map(int,input().split())

num = [i for i in range(1, a+1)]
pick = []


def backtrack(num, b, pick):
    # 종료조건
    if len(pick) == b:
        print(*pick)
        return
    
    for i in num:
        if i == "*":
            continue

        if pick and pick[-1] > i:
            continue
        
        pick.append(i)
        num[i-1] = "*"

        backtrack(num, b, pick)

        pick.pop()
        num[i-1] = i

backtrack(num, b, pick)