# Z
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

base = [[0,1],
        [2,3]]

divide = 2**(n-1)
multiple = 4**(n-1)

base_num = 0

while divide >= 1:
    n_r = r // divide
    n_c = c // divide

    base_num += multiple * (base[n_r][n_c])

    r -= n_r * divide
    c -= n_c * divide
    divide //= 2
    multiple //= 4
    
print(base_num)
