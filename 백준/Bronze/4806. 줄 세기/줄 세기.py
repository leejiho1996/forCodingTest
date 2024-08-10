import sys
cnt=0
while True:
    try:
        text=input()
        cnt+=1
    except:
        break
print(cnt)