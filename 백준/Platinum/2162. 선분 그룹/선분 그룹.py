# 라이브러리 세팅
import sys

# ccw 함수
def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

# 선분 교차여부 함수
def if_cross(first, second):

    # 변수 세팅
    x1, y1, x2, y2 = map(int, first)
    one = [x1, y1]
    two = [x2, y2]
    x3, y3, x4, y4 = map(int, second)
    three = [x3, y3]
    four = [x4, y4]

    # 예외처리(같은 직선상에 있는 경우)
    if (ccw(one, two, three) == 0) & (ccw(one, two, four) == 0) & (ccw(three, four, one) == 0) & (ccw(three, four, two) == 0):
        line_1 = [one, two] 
        line_2 = [three, four]
        line_1.sort(key=lambda x:(x[0]))
        line_2.sort(key=lambda x:(x[0]))
        if (line_1[0][0] > line_2[1][0]) | (line_1[1][0] < line_2[0][0]):
            return False
        line_1.sort(key=lambda x:(x[1]))
        line_2.sort(key=lambda x:(x[1]))
        if (line_1[0][1] > line_2[1][1]) | (line_1[1][1] < line_2[0][1]):
            return False
        else:
            return True

    # ccw를 이용하여 교차여부 탐색
    if (ccw(one, two, three) * ccw(one, two, four) <= 0) & (ccw(three, four, one) * ccw(three, four, two) <= 0):
        return True
    else:
        return False
    
# 변수 세팅
n = int(sys.stdin.readline())
union = [i for i in range(n)]

# 루트 탐색 함수
def findp(k):
    if k == union[k]:
        return k
    union[k] = findp(union[k])
    return union[k]

# 유니온 파인드를통해 교차하는 선분
line_list = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    line_list.append(list(line))
    for j in range(i):
        if if_cross(line, line_list[j]):
            p1 = findp(i) 
            p2 = findp(j)
            if p1 != p2:
                union[p1] = p2

# 루트 갱신
for i in range(n):
    findp(i)

# 답세팅, 출력
group = set(union)
group_num = len(group)
ma = 0
for i in group:
    k = union.count(i)
    ma = max(ma, k)
print(group_num)
print(ma)