# 합
import sys
input = sys.stdin.readline

L, U = map(int,input().split())

def solve(N):
    strN = str(N)
    length = len(strN)
    # num_cnt[i] => 10^i-1 까지 1-9가 모두 한번씩 나오는 횟수
    num_cnt = [0] * 11
    num_cnt[1] = 1
    one_to_nine = 0 # 1-9가 모두 한번씩 나오는 횟수
    result = [0] * 10
    cnt = 0
     
    if N < 10:
        for i in range(1, N+1):
            cnt += i 

        return cnt

    # 10^(i-1)-1 까지 1-9가 모두 나오는 횟수를 계산
    for i in range(2, 11):
        num_cnt[i] = num_cnt[i-1] * 10 + 10**(i-1)
        
    for i in range(length-1):
        cur = int(strN[i])
        # 현재 숫자가 0인 경우는 continue
        if cur == 0:
            continue
        # 현재 숫자는 뒤에 숫자+1 만큼 추가적으로 나온다
        result[cur] += int(strN[i+1:])+1
        # 1-9가 모두 한번씩 나오는 횟수 계산
        one_to_nine += cur * num_cnt[length-i-1]

        # 현재자리수에서 1에서 현재숫자-1이 나오는 횟수 계산 
        for j in range(1, cur):
            result[j] += 10**(length-i-1)

    # 일의자리 숫자 계산
    for i  in range(1, int(strN[-1])+1):
        result[i] += 1

    # 1-9가 나온 횟수를 더해준다
    for i in range(1, 10):
        result[i] += one_to_nine

    for i in range(1, 10):
        cnt += result[i] * i

    return cnt

print(solve(U) - solve(L-1))
