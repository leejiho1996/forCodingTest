values = ['' for _ in range(50 * 50)]
parent = [i for i in range(50 * 50)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x1, x2):
    root1 = find(x1)
    root2 = find(x2)

    if not values[root1] and values[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1


def solution(commands):
    answer = []

    for command in commands:
        command = list(command.split())
        if command[0] == 'UPDATE':
            if len(command) == 4:   # r, c의 root value만을 바꿔준다.
                r, c, value = command[1:]
                r, c = int(r) - 1, int(c) - 1
                x = r * 50 + c
                rootx = find(x)
                values[rootx] = value

            else: # value1을 모두 찾아, value2로 바꿔준다.
                value1, value2 = command[1:]
                for i in range(50 * 50):
                    if values[i] == value1:
                        values[i] = value2

        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = map(lambda x: int(x) - 1, command[1:])

            x1 = r1 * 50 + c1
            x2 = r2 * 50 + c2
            if parent[x1] != parent[x2]:
                union(x1, x2)

        elif command[0] == 'UNMERGE':
            r, c = map(lambda x: int(x) - 1, command[1:])
            x = r * 50 + c
            rootx = find(x)
            valuex = values[rootx]

            nodes = []
            for i in range(50 * 50):
                if find(i) == rootx:
                    nodes.append(i)

            for node in nodes:
                values[node] = ''
                parent[node] = node

            values[x] = valuex

        elif command[0] == 'PRINT':
            r, c = map(lambda x: int(x) - 1, command[1:])
            x = r * 50 + c
            rootx = find(x)

            if not values[rootx]:
                answer.append('EMPTY')
            else:
                answer.append(values[rootx])

    return answer