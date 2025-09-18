import sys
input = sys.stdin.readline
INF = 10**18

class GasStation:
    def __init__(self, x, p):
        self.x = x
        self.p = p

def main():
    C, E, D = map(int, input().split())
    N = int(input())

    gs = [None] * (N + 2)
    gs[0] = GasStation(0, 0)
    gs[N + 1] = GasStation(D, 0)

    if N != 0:
        dists = list(map(int, input().split()))
        costs = list(map(int, input().split()))
        for i in range(1, N + 1):
            x = gs[i - 1].x + dists[i - 1]
            p = costs[i - 1]
            gs[i] = GasStation(x, p)

    
    dp = [[INF] * (C + 1) for _ in range(N + 2)]
    
    fgs = C - (gs[1].x * E) 
    if fgs < 0:
        print(-1)
        return

    dp[1][fgs] = 0

    for i in range(1, N + 1):
        for j in range(C + 1):
            if dp[i][j] != INF:
                nd = gs[i + 1].x - gs[i].x  
                for k in range(C - j + 1):  
                    curFuel = j + k
                    curFuel -= nd * E
                    if curFuel >= 0:
                        dp[i + 1][curFuel] = min(dp[i + 1][curFuel], dp[i][j] + gs[i].p * k)

    answer = min(dp[N + 1])
    if answer == INF:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()
