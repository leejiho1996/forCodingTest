# A를 B로
import sys
input = sys.stdin.readline

init = input().rstrip()
target = input().rstrip()
result = 0

# 두 문자에 들어있는 문자가 서로 다르면 -1 출력 후 종료
sort1 = sorted(list(init))
sort2 = sorted(list(target))

for i in range(len(init)): 
    if sort1[i] != sort2[i]:
        print(-1)
        exit()

tidx = len(init) - 1

# target 문자를 만들기 위해 꼭 이동해야하는 문자의 갯수를 구한다
for idx in range(len(init)-1, -1, -1):
    if (init[idx] == target[tidx]): # 문자가 서로 같다면 target의 인덱스 - 1
        tidx -= 1
    else:
        result += 1 # 문자가 서로 다르다면 문자를 옮겨야하니 result + 1

print(result)
