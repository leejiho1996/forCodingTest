# Expected Error
import sys
input = sys.stdin.readline

N, K, P = map(int,input().split())

continu = (N - K) * 1 + 1
backspace = (N - K) * 1 + 1 + 1
restart = 3 + N * 1 + 1

success = continu * ((100 - P)/100) + (continu + restart) * (P/100)
backspace = backspace * (P/100) + (backspace + restart) * ((100-P)/100)

result = min(success, backspace, restart)

if result == success:
    print("continue")
elif result == backspace:
    print("backspace")
else:
    print("restart")

# restart = 0.3
# typing or backsapce or submitting = 0.1
# submit wrong password = 0.3
