# 잠수함 식별
import sys
input = sys.stdin.readline

def dfs(string, idx):

    result = 0

    if string[idx] == '1':

        if len(string) - idx <= 2:
            return 0

        if string[idx+1] != '0' or string[idx+2] != '0':
            return 0

        for i in range(idx+3, len(string)):
            if string[i] == '1':
                if i == len(string) - 1:
                    return 1
                elif string[i+1] == '0':
                    result = max(result, dfs(string, i+1))
                    break
                else:
                    result = max(result, dfs(string, i+1))

        return result
                
    if string[idx] == '0':

        if len(string) - idx <= 1:
            return 0

        if string[idx+1] != '1':
            return 0

        if string[idx+1] == '1' and idx+1 == len(string)-1:
            return 1
        
        return dfs(string, idx+2)
    
string = input().rstrip()

if dfs(string, 0):
    print("SUBMARINE")
else:
    print("NOISE")
