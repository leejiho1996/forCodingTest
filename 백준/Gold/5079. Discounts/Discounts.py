# Discounts
import sys
input = sys.stdin.readline

while True:
    product = input().rstrip()

    if product == "#":
        break
    
    d, p = map(int,input().split())
    price = d * 100 + p

    D = int(input())
    promotions = []

    # dp[i] => i개의 물건을 샀을때 그 중 증정으로 가져갈수 있는 물건의 최대값
    dp = [0] * 501
    
    for i in range(D):
        B, F = map(int,input().split())
        promotions.append((B, F))
        
    E = int(input())

    for i in range(1, 501):
        for j in range(D):
            b, f = promotions[j]
            # 추가로 주는 물건을 모두 다 가져가지 않아도 되므로 하나씩 계산 
            for k in range(f+1):

                if i - (b + k) < 0:
                    continue
            
                dp[i] = max(dp[i], dp[i-(b+k)] + k)
            
    print(product)
    for i in range(E):
        buy = int(input())
        saved = dp[buy] * price / 100
        print(f'Buy {buy}, save ${saved:.2f}')
