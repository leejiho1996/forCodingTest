import sys
input = sys.stdin.readline

while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
        
    if a + b == 13:
        print("Never speak again.")
    elif a > b:
        print("To the convention.")
    elif a < b:
        print("Left beehind.")
    else:
        print("Undecided.")