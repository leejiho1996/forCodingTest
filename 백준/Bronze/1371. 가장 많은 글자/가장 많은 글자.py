al_count = [0]*26
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:                                      #추가 내용
    try:                                         #추가 내용
        sentense = input()
        for i in range(len(al)):
            al_count[i] += sentense.count(al[i])
    except EOFError:                             #추가 내용
        break                                    #추가 내용
search = max(al_count)
for i in range(len(al_count)):
    if al_count[i] == search:
        print(al[i], end='')
