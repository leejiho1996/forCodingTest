import sys
input = sys.stdin.readline

for i in range(3):
    word = input().rstrip()
    if word not in ["FizzBuzz", "Fizz", "Buzz"]:
        answer = int(word) + 3 - i
        break

if answer % 15 == 0:
    print("FizzBuzz")
elif answer % 3 == 0:
    print("Fizz")
elif answer % 5 == 0:
    print("Buzz")
else:
    print(answer)