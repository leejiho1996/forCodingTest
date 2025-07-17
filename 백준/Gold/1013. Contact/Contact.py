#Contact

import sys
input = sys.stdin.readline

def dfs(string, idx):
    # 현재 숫자가 1인경우
    if string[idx] == '1':
        ret = 0 # 리턴할 초기 값 0

        # 남은 숫자가 2개 미만이라면 0 리턴
        if len(string) - idx <= 2:
            return 0
        # 뒤 두개의 숫자가 0이 아니라면 0 리턴
        if string[idx+1] != '0' or string[idx+2] != '0':
            return 0

        # 2칸 뒤 부터 탐색
        for i in range(idx+3, len(string)):
            # 1이 나온 경우
            if string[i] == '1':
                # 마지막이라면 1 리턴
                if i == len(string) - 1:
                    return 1
                # 다음숫자가 0이라면 패턴이 끝났으니 다음 탐색하고 반복문 멈춤
                elif string[i+1] == '0':
                    ret = max(ret, dfs(string, i+1))
                    break
                else: # 1이 계속 이어진다면 각 부분마다 끊어서 확인
                    ret = max(ret, dfs(string, i+1))

        return ret

    # 현재 숫자가 0인 경우       
    if string[idx] == '0':
        # 남은 숫자가 없거나 다음 숫자가 1이 아니라면 0 리턴
        if idx == len(string) - 1 or string[idx+1] != '1':
            return 0
        # 다음 숫자가 1이면서 마지막이라면 1 리턴
        if string[idx+1] == '1' and idx+1 == len(string)-1:
            return 1

        # 다음 숫자가 1이면서 아직 끝이 아니라면 남은 부분 탐색
        return dfs(string, idx+2)
    
N = int(input())

for i in range(N):
    string = input().rstrip()

    if dfs(string, 0):
        print("YES")
    else:
        print("NO")
