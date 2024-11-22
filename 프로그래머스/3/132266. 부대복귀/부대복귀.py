import heapq as hq

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for start, to in roads:
        graph[start].append(to)
        graph[to].append(start)
    
    visited = [0] * (n+1)
    que = [(1, destination)]
    
    while que:
        cost, cur = hq.heappop(que)

        if visited[cur]:
            continue

        visited[cur] = cost

        for j in graph[cur]:
            if visited[j]:
                continue

            hq.heappush(que, (cost+1, j))
    
    for i in sources:
        if visited[i] == 0:
            answer.append(-1)
        else:
            answer.append(visited[i]-1)        

    return answer