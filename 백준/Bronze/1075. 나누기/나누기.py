# 입력을 받아야 합니다
N = int(input())
F = int(input())

# N의 뒤 두 자리를 00으로 만듭니다
N = (N//100) * 100

# 0부터 99까지 순회하며 F로 나누어 떨어지는지 확인합니다
for i in range(100):
   if (N + i) % F == 0:
      # 결과 출력 (두 자리 형식으로 맞추기)
      print(str(i).zfill(2))
      break