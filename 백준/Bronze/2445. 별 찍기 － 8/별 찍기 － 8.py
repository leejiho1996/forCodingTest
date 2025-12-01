N = int(input())

for i in range(N*2-1):
    if i < N:
        print("*"*(i+1), ' '*(2*N-2*(i+1)), "*"*(i+1), sep="")
    else:
        print("*"*(2*N-i-1), ' '*((i-N+1)*2), "*"*(2*N-i-1), sep="")
