# 홍준 프로그래밍 대회
import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int,input().split()))
maxx = max(students)
exists = [0] * (maxx+1)
yaksu = [0] * (maxx+1)
yaksu[1] = N

for i in range(N):
    exists[students[i]] += 1

for i in range(2, maxx+1):
    cur = i
    # 현재 수로 만들 수 있는 모든 배수 탐색
    while cur <= maxx:
        # 해당 수가 존재한다면 해당 수 갯수만큼 더해준다
        if exists[cur]:
            yaksu[i] += exists[cur]
        
        cur += i # i만큼 증가시켜 다음 배수 확인
        
result = 0
for i in range(1, maxx+1):
    if yaksu[i] < 2: # 2팀이상은 진출해야하므로 체크
        continue
    # result => 팀당 인원수 * 가능한 학교 수
    result = max(result, yaksu[i] * i)
    
print(result)
