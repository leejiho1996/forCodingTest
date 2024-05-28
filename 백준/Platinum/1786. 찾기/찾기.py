# 찾기
import sys
input = sys.stdin.readline

def preKMP(target):
    length = len(target)
    f = [-1] * length
    idx = -1
    
    for i in range(1, length):
        while idx >= 0 and target[i] != target[idx+1]:
            idx = f[idx]
        
        if target[i] == target[idx+1]:
            idx += 1

        f[i] = idx
        
    return f

def KMP(sentence, target):
    f = preKMP(target)

    s_idx = 0
    t_idx = 0
    cnt = 0

    result = []
    
    while True:
        if s_idx >= len(sentence):
            break
        
        if sentence[s_idx] == target[t_idx]:
            s_idx += 1
            t_idx += 1
            
            if t_idx == len(target):
                result.append(s_idx-len(target)+1)
                cnt += 1
                t_idx = f[t_idx-1] + 1
    
        else:
            if t_idx == 0: # target 인덱스가 0이라면 그냥 다음 문자열 찾기
                s_idx += 1
                continue
            
            if f[t_idx-1] == -1:
                t_idx = 0
              
            else:
                t_idx = f[t_idx-1] + 1
        
    print(cnt)

    return result
           
sentence = input().rstrip("\n")
target = input().rstrip("\n")

result = KMP(sentence, target)

print(*result)
