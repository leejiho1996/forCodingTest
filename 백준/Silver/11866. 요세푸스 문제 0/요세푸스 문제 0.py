#요세푸스 문제 0

n, k = map(int,input().split())

yo = [i for i in range(1, n+1)]

cnt = 0
start = 0

printing = []

while yo:
    start = (start + (k - 1)) % len(yo)
    printing.append(str(yo[start]))    
    del yo[start]

number = ", ".join(printing)

print('<'+ number + '>')
