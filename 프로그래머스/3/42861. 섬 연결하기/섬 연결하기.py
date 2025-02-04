import heapq as hq

parent= []

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    
    return parent[n]


def solution(n, costs):
    global parent
    
    answer = 0
    costs.sort(key = lambda x : x[2])
    
    parent = [i for i in range(n+1)]
    
    for i in costs:
        start, to, cost = i[0], i[1], i[2]
        ps = find(start)
        pt = find(to)
        
        if ps != pt:
            answer += cost
            parent[ps] = pt
            
    return answer