scores = list(map(int,input().split()))
scores.sort()

print(abs((scores[0] + scores[-1]) - (scores[1] + scores[2])))