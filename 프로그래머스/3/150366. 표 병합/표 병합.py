def dfs(stack, visited, word, unmerge=0):
    while stack:
        num = stack.pop()
        if visited[num]:
            continue
        else:
            visited[num] = 1
            
        graph[num] = word
        
        for i in merge[num]:
            if visited[i]:
                continue
            stack.append(i)
        
        if unmerge:
            merge[num] = []

def doMerge(cell1, cell2): # cell2를 cell1으로 바꿈
    visited = [0] * 2500
    stack = [cell2]
    content = graph[cell1]
    dfs(stack, visited, content)
        
def doUnmerge(cell):
    visited = [0] * 2500
    visited[cell] = 1
    stack = []
    
    for i in merge[cell]:
        stack.append(i)
    
    merge[cell] = []
    dfs(stack, visited, "", 1)
        
def Update(cell, word):
    graph[cell] = word
    visited = [0] * 2500
    visited[cell] = 1
    stack = []
    
    for i in merge[cell]:
        stack.append(i)
    
    dfs(stack, visited, word)

graph = [""] * 2500
merge = [[] for _ in range(2500)]
        
def solution(commands):
    answer = []
    
    for i in commands:
        command = i.split(" ")
        
        if command[0] == "UPDATE" and len(command) == 4:
            r, c = int(command[1])-1, int(command[2])-1
            cell = r*50+c
            Update(cell, command[3])
        
            
        elif command[0] == "UPDATE" and len(command) == 3:
            for i in range(2500):
                if graph[i] == command[1]:
                    graph[i] = command[2]
            
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = map(int, command[1:])
            cell1 = (r1-1) * 50 + c1-1
            cell2 = (r2-1) * 50 + c2-1
            
            if cell1 == cell2 : # r, c가 동일하면 스킵
                continue
                
            elif graph[cell1] != "" and graph[cell2] == "":  # 셀1 만 값을 가질 경우
                doMerge(cell1, cell2)
            
            elif graph[cell1] == "" and graph[cell2] != "": # 셀2 만 값을 가질 경우
                doMerge(cell2, cell1)
                
            else: # 둘다 있거나 없다면 셀1값으로 가짐
                doMerge(cell1, cell2)
                
            merge[cell1].append(cell2)
            merge[cell2].append(cell1)
            
        elif command[0] == "UNMERGE":
            r, c = int(command[1])-1, int(command[2])-1
            cell = r * 50 + c
            doUnmerge(cell)
                
        elif command[0] == "PRINT":
            r, c = int(command[1])-1, int(command[2])-1
            word = graph[r * 50 + c]
            if word == "":
                answer.append("EMPTY")
            else:
                answer.append(word)
        
    return answer