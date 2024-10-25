def solution(cap, n, deliveries, pickups):
    answer = 0
    total_deliveries = sum(deliveries)
    total_pickups = sum(pickups)
    
    last_delivery_index = n - 1
    last_pickup_index = n - 1
    
    # 가장 마지막 배달/수거 위치 찾기
    while last_delivery_index >= 0 and deliveries[last_delivery_index] == 0:
        last_delivery_index -= 1
    while last_pickup_index >= 0 and pickups[last_pickup_index] == 0:
        last_pickup_index -= 1
    
    while total_deliveries > 0 or total_pickups > 0:
        # 이번 왕복에서 배달/수거할 수 있는 최대량 설정
        delivery_capacity = cap
        pickup_capacity = cap

        # 왕복 거리 계산
        answer += (max(last_delivery_index, last_pickup_index) + 1) * 2
        
        # 배달 작업
        for i in range(last_delivery_index, -1, -1):
            if deliveries[i] <= delivery_capacity:
                delivery_capacity -= deliveries[i]
                total_deliveries -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= delivery_capacity
                total_deliveries -= delivery_capacity
                delivery_capacity = 0
                last_delivery_index = i
                break
        else:
            last_delivery_index = -1

        # 수거 작업
        for i in range(last_pickup_index, -1, -1):
            if pickups[i] <= pickup_capacity:
                pickup_capacity -= pickups[i]
                total_pickups -= pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= pickup_capacity
                total_pickups -= pickup_capacity
                pickup_capacity = 0
                last_pickup_index = i
                break
        else:
            last_pickup_index = -1

    return answer
