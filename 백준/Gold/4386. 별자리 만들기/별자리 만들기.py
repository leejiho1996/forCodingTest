# 별자리
import sys
input = sys.stdin.readline

n = int(input())

stars = []
distances = []
stars_parent = [i for i in range(n)]

for i in range(n):
    x, y = map(float,input().split())
    stars.append((x,y,i)) # i는 별들의 인덱스

for i in range(n):
    x1, y1, idx1 = stars[i]
    for j in range(i+1, n):
        x2, y2, idx2 = stars[j]
        distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
        distances.append((distance, idx1, idx2))

distances.sort(key = lambda x:x[0], reverse=True)

def find(idx):
    if stars_parent[idx] != idx:
        stars_parent[idx] = find(stars_parent[idx])

    return stars_parent[idx]

total = 0

while distances:
    distance, star1, star2 = distances.pop()
    
    parent1 = find(star1)
    parent2 = find(star2)

    if parent1 == parent2:
        continue
    
    if parent1 != parent2:
        stars_parent[parent2] = parent1
        total += distance

print(f'{total:.2f}')
