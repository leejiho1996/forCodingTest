import sys
input = sys.stdin.readline

for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int,input().split())
    
    ss = h1 * 3600 + m1 * 60 + s1
    es = h2 * 3600 + m2 * 60 + s2
    
    term = es - ss
    
    print(term//3600, term%3600//60, term%3600%60)