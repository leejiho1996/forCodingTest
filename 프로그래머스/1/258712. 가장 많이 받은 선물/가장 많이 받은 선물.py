def solution(friends, gifts):
    sequence = {}
    graph = [[0]*len(friends) for i in range(len(friends))]
    gift = {}
    check = []
    for i, n in enumerate(friends):
        sequence[n] = i
        gift[n] = [0,0,0]
    for i in gifts:
        k = i.split()
        give = k[0]
        get = k[1]
        gift[give][0] += 1
        gift[get][1] += 1
        gift[give][2] = gift[give][0] - gift[give][1]
        gift[get][2] = gift[get][0] - gift[get][1]
        graph[sequence[give]][sequence[get]] += 1
    for i in range(len(graph)):
        get_gift = 0
        for j in range(len(graph)):
            if i == j:
                continue
            if graph[i][j] > graph[j][i]:
                get_gift += 1
            elif graph[i][j] == graph[j][i] and gift[friends[i]][2] > gift[friends[j]][2]:
                get_gift+=1
        check.append(get_gift)
    return max(check)
