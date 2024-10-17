# 비슷한 단어
import sys
input = sys.stdin.readline

class Node():
    def __init__(self, data):
        self.data = data
        self.child = {}

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, char):
        cur = self.head
        cnt = 0
        for i in char:
            if i not in cur.child:
                cur.child[i] = Node(i)
            else:
                cnt += 1  
            cur = cur.child[i]
        return cnt
        
n = int(input())
t = Trie()
maxx = 0
char_list = []
childs = []
for i in range(n):
    char = input().rstrip()
    cnt = t.insert(char)
    char_list.append(char)
    
    if cnt >= maxx:
        if cnt == maxx:
            childs.append(char)
        else:
            maxx = cnt
            childs = [char]
            
first = 20001
for child in childs:
    for i in range(n):
        parent = char_list[i]
        if child == parent or len(parent) < maxx:
            continue
        check = True
        
        for j in range(maxx):
            if child[j] != parent[j]:
                check = False
                break
            
        if check == True:
            if first > i:
                result = [parent, child]
                first = i
            break

print(result[0])
print(result[1])
