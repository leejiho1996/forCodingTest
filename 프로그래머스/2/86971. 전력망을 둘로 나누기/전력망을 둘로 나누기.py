def dfs(n, graph):
    visited = [0] * (n+1)
    result = []
    for j in range(1, n+1):
        if visited[j]:
            continue
        stack = [j]
        cnt = 0

        while stack:
            cur = stack.pop()

            if visited[cur]:
                continue
            else:
                visited[cur] = 1
                cnt += 1

            for k in range(1, n+1):
                if graph[cur][k] and visited[k] == 0:
                    stack.append(k)
                    
        result.append(cnt)
    
    return (abs(result[0] - result[1]))

def solution(n, wires):
    answer = 101
    
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for i in wires:
        start = i[0]
        end = i[1]
        graph[start][end] = 1
        graph[end][start] = 1
        
    for i in wires:
        start = i[0]
        end = i[1]
        visited = [0] * (n+1)
        graph[start][end] = 0 # 그래프 연결을 끊어준다
        graph[end][start] = 0
        
        result = dfs(n, graph)        
        
        graph[start][end] = 1 # 그래프 연결 다시 복구
        graph[end][start] = 1
        answer = min(answer, result)
        
    return answer