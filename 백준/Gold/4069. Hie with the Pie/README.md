# [Gold IV] Hie with the Pie - 4069 

[문제 링크](https://www.acmicpc.net/problem/4069) 

### 성능 요약

메모리: 32412 KB, 시간: 4168 ms

### 분류

백트래킹, 브루트포스 알고리즘, 플로이드–워셜, 그래프 이론, 최단 경로, 외판원 순회 문제

### 제출 일자

2025년 5월 12일 17:21:22

### 문제 설명

<p>The Pizazz Pizzeria prides itself in delivering pizzas to its customers as fast as possible. Unfortunately, due to cutbacks, they can afford to hire only one driver to do the deliveries. He will wait for 1 or more (up to 10) orders to be processed before he starts any deliveries. Needless to say, he would like to take the shortest route in delivering these goodies and returning to the pizzeria, even if it means passing the same location(s) or the pizzeria more than once on the way. He has commissioned you to write a program to help him.</p>

### 입력 

 <p>Input will consist of multiple test cases. The first line will contain a single integer n indicating the number of orders to deliver, where 1 ≤ n ≤ 10. After this will be n + 1 lines each containing n + 1 integers indicating the times to travel between the pizzeria (numbered 0) and the n locations (numbers 1 to n). The j<sup>th</sup> value on the i<sup>th</sup> line indicates the time to go directly from location i to location j without visiting any other locations along the way. Note that there may be quicker ways to go from i to j via other locations, due to different speed limits, traffic lights, etc. Also, the time values may not be symmetric, i.e., the time to go directly from location i to j may not be the same as the time to go directly from location j to i. An input value of n = 0 will terminate input.</p>

### 출력 

 <p>For each test case, you should output a single number indicating the minimum time to deliver all of the pizzas and return to the pizzeria.</p>

