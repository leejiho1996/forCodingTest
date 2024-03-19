a, b = map(int,input().split())

card = list(map(int,input().split()))

mx = sum(card)

for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            if card[i] + card[j] + card[k] > b:
                pass
            else:
                n = b - (card[i] + card[j] + card[k])
                if n < mx:
                    black = card[i] + card[j] + card[k]
                    mx = n

print(black)
