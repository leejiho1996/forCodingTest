primeNum = []
visited = []
prime = 0
num_visited = []

def backtrack(num, numbers):
    global cnt
    global prime
    
    if len(num) > len(numbers):
        return
    
    if len(num) > 0 and not visited[int(num)]:
        visited[int(num)] = 1
        if not primeNum[int(num)]:
            prime += 1
    
    for i in range(len(numbers)):
        if num_visited[i]:
            continue
        num_visited[i] = 1
        backtrack(num + numbers[i], numbers)
        num_visited[i] = 0
        
def solution(numbers):
    global num_visited
    global primeNum
    global visited
    
    answer = 0
    word = []
    
    for i in numbers:
        word.append(i)
        
    word.sort(reverse=True)
    maxNum = int("".join(word)) + 1
    
    num_visited = [0] * len(numbers)
    visited = [0] * maxNum
    primeNum = [0] * maxNum
    primeNum[0] = 1
    primeNum[1] = 1
    
    
    for i in range(2, maxNum):
        if primeNum[i] == 0:
            cnt = 2
            while True:
                if i * cnt >= maxNum:
                    break
                    
                primeNum[i*cnt] = 1
                cnt += 1
    
    backtrack("", numbers)
    
    return prime