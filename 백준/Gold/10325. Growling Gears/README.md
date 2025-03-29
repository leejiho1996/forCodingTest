# [Gold V] Growling Gears - 10325 

[문제 링크](https://www.acmicpc.net/problem/10325) 

### 성능 요약

메모리: 14188 KB, 시간: 100 ms

### 분류

수학

### 제출 일자

2025년 3월 29일 23:41:34

### 문제 설명

<p>The Best Acceleration Production Company specializes in multi-gear engines. The performance of an engine in a certain gear, measured in the amount of torque produced, is not constant: the amount of torque depends on the RPM of the engine. This relationship can be described using a torque-RPM curve.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/growing.png" style="height:291px; width:483px"></p>

<p style="text-align: center;">The torque-RPM curve of the gears given in the second sample input.<br>
The second gear can produce the highest torque.</p>

<p>For the latest line of engines, the torque-RPM curve of all gears in the engine is a parabola of the form T = -aR<sup>2</sup> + bR + c, where R is the RPM of the engine, and T is the resulting torque.</p>

<p>Given the parabolas describing all gears in an engine, determine the gear in which the highest torque is produced. The first gear is gear 1, the second gear is gear 2, etc. There will be only one gear that produces the highest torque: all test cases are such that the maximum torque is at least 1 higher than the maximum torque in all the other gears.</p>

### 입력 

 <p>On the first line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with a single integer n (1 ≤ n ≤ 10): the number of gears in the engine.</li>
	<li>n lines, each with three space-separated integers a, b and c (1 ≤ a, b, c ≤ 10 000): the parameters of the parabola T = -aR<sup>2</sup> +bR+c describing the torque-RPM curve of each engine.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with a single integer: the gear in which the maximum torque is generated.</li>
</ul>

