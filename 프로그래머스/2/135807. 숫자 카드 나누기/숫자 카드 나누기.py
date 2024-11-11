
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
from math import gcd

def get_gcd(arr):
    g = arr[0]
    for i in range(len(arr)):
        g = gcd(g, arr[i])
    return g


def solution(arrayA, arrayB):
    answer = 0
    gA, gB = get_gcd(arrayA), get_gcd(arrayB)

    for b in arrayB:
        if not b % gA:
            break
    else:
        answer = max(answer, gA)

    for a in arrayA:
        if not a % gB:
            break
    else:
        answer = max(answer, gB)

    return answer
