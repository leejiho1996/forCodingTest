# 큐
import sys
input = sys.stdin.readline

class Que:
    
    def __init__(self, size):
        self.que = [0] * size
        self.head = 0
        self.tail = 0

    def push(self, num):
        self.que[self.tail] = num
        self.tail += 1

    def pop(self):
        if (self.tail - self.head) == 0:
            print(-1)
        else:
            print(self.que[self.head])
            self.head += 1

    def size(self):
        print(self.tail - self.head)

    def empty(self):
        if (self.tail - self.head) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if (self.tail - self.head) == 0:
            print(-1)
        else:
            print(self.que[self.head])

    def back(self):
        if (self.tail - self.head) == 0:
            print(-1)
        else:
            print(self.que[self.tail-1])

n = int(input())
que = Que(n)

for i in range(n):
    c = input().rstrip()
    command = c.split(" ")

    if command[0] == "push":
        que.push(command[1])
    elif command[0] == "pop":
        que.pop()
    elif command[0] == "size":
        que.size()
    elif command[0] == "empty":
        que.empty()
    elif command[0] == "front":
        que.front()
    else:
        que.back()
