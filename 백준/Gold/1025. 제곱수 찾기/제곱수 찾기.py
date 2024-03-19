# 제곱수 찾기

a, b = map(int,input().split())
board = []
mx = []
for i in range(a):
    board.append(list((input())))

mx = -1

for i in range(a):
    for j in range(b):
        for k in range(-a, a):
            for l in range(-b, b):
                if k == 0 and l == 0:
                    continue
                num =''
                x = i
                y = j

                while True:
                    num += board[x][y]
                    if int(int(num)**(1/2)) == (int(num)**(1/2)):
                        mx = max(mx, int(num))
                    if x + k < 0 or y + l < 0 or x + k >= a or y + l >= b:
                        break
                    else:
                        x += k
                        y += l
print(mx)