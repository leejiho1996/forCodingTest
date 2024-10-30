def hanoi(answer, k, cur, sub, main):
    if k == 1:
        answer.append([cur, main]) # k가 1 이라면 바로 main으로 옮기면 됨
        return
    
    hanoi(answer, k-1, cur, main, sub) # 위에 원판이 있다면 main을 거쳐 sub로 옮겨줘야함
    answer.append([cur, main]) # 다 옮긴 다음 가장 큰 원판을 main으로 옮겨줌
    hanoi(answer, k-1, sub, cur, main) # sub에 있는 원판을 cur을 거쳐 main으로 옮겨줌
    
def solution(n):
    answer = []
    hanoi(answer, n, 1, 2, 3)
    return answer