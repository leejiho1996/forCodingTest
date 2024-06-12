# LCS 2
import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

word_graph = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

for i in range(len(word1)):
    char1 = word1[i]
    for j in range(len(word2)):
        char2 = word2[j]

        if char1 == char2:
            word_graph[i+1][j+1] = word_graph[i][j] + 1
        else:
            word_graph[i+1][j+1] = max(word_graph[i][j+1], word_graph[i+1][j])
            
i = len(word1) 
j = len(word2)

subseq = []

while True:
    
    if word_graph[i][j] == 0:
        break

    if word_graph[i-1][j] == word_graph[i][j]:
        i -= 1
    elif word_graph[i][j-1] == word_graph[i][j]:
        j -= 1
    else:
        subseq.append(word1[i-1])
        i -= 1
        j -= 1

   
print(len(subseq))
print(*subseq[::-1],sep="")     
