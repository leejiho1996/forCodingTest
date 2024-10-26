def solution(targets):
    cnt = 0
    targets.sort()
    shot = 0
    for s, e in targets:
    
        if shot <= s:
            cnt += 1
            shot = e
        else:
            shot = min(shot, e)
    return cnt