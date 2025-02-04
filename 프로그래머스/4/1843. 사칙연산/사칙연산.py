def solution(arr):
    answer = -1
    nums = []
    operators = []
    
    for i in range(len(arr)):
        if i % 2 == 0:
            nums.append(int(arr[i]))
        else:
            operators.append(arr[i])
    
    num_length = len(nums)
    # dp[i][j] => i번째 수부터 j번째 수까지 연산했을때 최대값
    dpMax = [[-100001] * num_length for _ in range(num_length)]
    dpMin = [[100001] * num_length for _ in range(num_length)]
    
    for i in range(num_length):
        dpMax[i][i] = nums[i]
        dpMin[i][i] = nums[i]
    
    for i in range(1, num_length):
        for j in range(num_length - i):
            # [0][1], [1][2], [2][3]
            # [0][2], [1][3] ... 이런 순으로 dp 채워감
            start = j 
            end = j + i
            for k in range(start, end):
                operator = operators[k]
                
                if operator == "+":
                    dpMax[start][end] = max(dpMax[start][end], dpMax[start][k] + dpMax[k+1][end])
                    dpMin[start][end] = min(dpMin[start][end], dpMin[start][k] + dpMin[k+1][end])
        
                else:
                    dpMax[start][end] = max(dpMax[start][end], dpMax[start][k] - dpMin[k+1][end])
                    dpMin[start][end] = min(dpMin[start][end], dpMin[start][k] - dpMax[k+1][end])
        
    return dpMax[0][len(nums)-1]