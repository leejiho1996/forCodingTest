def solution(targets):
    cnt = 0
    targets.sort()
    shot = 0
    for i in targets:
        s, e = i
        if shot <= s:
            cnt += 1
            shot = e
        else:
            shot = min(shot, e)
    return cnt