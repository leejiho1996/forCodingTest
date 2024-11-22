from collections import deque

def solution(edges):
    answer = [0, 0, 0, 0]
    LIMIT = 1000001
    graph = [[] for _ in range(LIMIT)]
    fan_in = [0] * LIMIT
    fan_out = [0] * LIMIT
    search = []
    
    maxx = 0
    for start, to in edges:
        graph[start].append(to)
        maxx = max(maxx, start, to)
        fan_out[start] += 1
        fan_in[to] += 1
    
    visited = [0] * (maxx+1)
    
    for i in range(1, maxx+1): # 진출 간선이 2개 이상인데 진입간선이 0개라면 신생 노드
        if fan_out[i] >= 2 and fan_in[i] == 0:
            answer[0] = i
            visited[i] = 1
            break
    
    for i in graph[answer[0]]:
        search.append(i)
    
    for i in search:
        if visited[i]:
            continue
        
        if len(graph[i]) == 1 and visited[graph[i][0]]:
            continue
            
        que = deque([])
        edge = 0
        node = 0
        que.append(i)
          
        
        while que:
            cur = que.popleft()
            
            if visited[cur]:
                continue
            else:
                visited[cur] = 1
                node += 1
            
            for j in graph[cur]:
                edge += 1

                if visited[j]:
                    continue
                    
                que.append(j)
        
        if node == edge:
            answer[1] += 1
        elif node-1 == edge:
            answer[2] += 1    
        elif (node-1)/2 == (edge-2) / 2:
            answer[3] += 1
        
    return answer