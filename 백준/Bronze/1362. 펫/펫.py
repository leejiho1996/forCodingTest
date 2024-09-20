target, now = map(int, input().split())
count = 1                          #해당 내용 추가
while target != 0 and now != 0:
    c = input().split()
    k = 0                          #해당 내용 추가
    while c[0] != '#' and c[1] != '0':
        if c[0] == 'F':
            now += int(c[1])
        elif c[0] == 'E':
            now -= int(c[1])
        if now <= 0:
            k += 1
        c = input().split()
    if k != 0:
        print(count, "RIP")
    else:
        if(target/2 < now < 2*target):
            print(count, ":-)")
        else:
            print(count, ":-(")
    target, now = map(int, input().split())
    count += 1