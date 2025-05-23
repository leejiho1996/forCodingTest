# [Gold III] 팬케이크 쌓기 - 12744 

[문제 링크](https://www.acmicpc.net/problem/12744) 

### 성능 요약

메모리: 102128 KB, 시간: 508 ms

### 분류

너비 우선 탐색, 자료 구조, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 7일 01:25:28

### 문제 설명

<p>지용이는 팬케이크를 잘 굽는 제빵사다. 어느 날, 지용이는 크기가 다른 앞뒤 구분이 되어있는 팬케이크를 N (1 ≤ N ≤ 6)개 만들었다. 이 N개의 팬케이크의 크기는 크기 순으로 정렬하면 1,2, … , N이다. 지용이는 생각 없이 팬케이크를 만들었기 때문에, 팬케이크를 만든 순서의 역순대로 팬케이크를 쌓아 놓았는데, 쌓아 놓은 순서가 팬케이크 크기 순이 아닐 수도 있다. 지용이는 최소 횟수의 뒤집기를 통해 팬케이크들이 위로 갈수록 크기가 작아지고, 모두 올바른 방향으로 쌓여지도록 만들고 싶다.</p>

<p>여기서 뒤집기란 다음과 같다: 1 ≤ i ≤ N인 임의의 i를 고르고 위에서부터 1 ~ i번째 팬케이크를 통째로 뒤집어서 순서를 완전히 거꾸로 바꾸고, 앞뒤 구분을 바꾼다. 예를 들어, i = 3을 골랐다면, 1(+) 2(+) 3(+) 4(+) 5(+) → 3(-) 2(-) 1(-) 4(+) 5(+)와 같이 팬케이크의 위치가 바뀐다. (여기서 +는 앞면, -는 뒷면을 의미한다)</p>

<p>이 문제를 해결하여 지용이를 도와주자</p>

### 입력 

 <p>첫 번째 줄에 N이 주어진다.</p>

<p>두 번째 줄부터 N + 1번째 줄에는 팬케이크의 크기와 현재 방향이 띄어쓰기로 구분되어 주어진다. (팬케이크의 방향은 앞면이라면 +, 뒷면이라면 -로 주어질 것이다.)</p>

### 출력 

 <p>조건을 만족하는 뒤집기의 최소 횟수를 구하여라.</p>

