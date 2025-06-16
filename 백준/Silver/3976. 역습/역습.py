# 역습
import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    N, L1, L2, S1, S2 = map(int,input().split())
    dp1 = [0] * 2
    dp2 = [0] * 2
    # 처음 값은 수비수로 부터 패스받은 L1, L2 
    dp1[0] = L1
    dp2[0] = L2

    # 1번 스트라이커의 패스와 드리블 난이도 
    S1Pass = list(map(int,input().split()))
    S1Drib = list(map(int,input().split()))
    # 2번 스트라이커의 패스와 드리블 난이도
    S2Pass = list(map(int,input().split()))
    S2Drib = list(map(int,input().split()))

    # 각 지점의 최소난이도는 드리블을 하거나 패스받은 경우 중 최소값
    for j in range(N-1):
        dp1[1] = min(dp1[0] + S1Drib[j], dp2[0] + S2Pass[j])
        dp2[1] = min(dp2[0] + S2Drib[j], dp1[0] + S1Pass[j])

        dp1[0] = dp1[1]
        dp2[0] = dp2[1]
        
    # 마지막에 슛을 하여 최소값을 출력
    print(min(dp1[0] + S1, dp2[0] + S2))
        
