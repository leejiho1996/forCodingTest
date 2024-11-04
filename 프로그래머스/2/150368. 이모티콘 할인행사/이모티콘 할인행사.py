
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
def make_percentage_cases(prev):
    cases = []
    for li in prev:
        for n in [40, 30, 20, 10]:
            cases.append(li + [n])
    return cases

def solution(users, emoticons):
    answer = []

    cases = [[]]  # 가능한 이모티콘별 할인율 케이스들
    for _ in range(len(emoticons)):
        cases = make_percentage_cases(cases)

    for case in cases:  # 완전 탐색
        result = [0, 0]
        for percentage, price in users:
            cost = 0
            for i in range(len(emoticons)):
                if case[i] >= percentage:  # 희망 할인율 이상이라면 구매
                    cost += emoticons[i] * (100 - case[i]) // 100
            if cost >= price:
                result[0] += 1
            else:
                result[1] += cost
        answer.append(result)
    answer.sort(key=lambda x:(-x[0], -x[1]))
    return answer[0]
