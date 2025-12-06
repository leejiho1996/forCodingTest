total = 0
for i in range(5):
    n = int(input())
    
    if n < 40:
        total += 40
    else:
        total += n
    
print(total//5)