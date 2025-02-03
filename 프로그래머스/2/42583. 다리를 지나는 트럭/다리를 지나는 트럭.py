def solution(bridge_length, weight, truck_weights):
    truckCnt = len(truck_weights)
    truckStart = []
    end = 0
    front = 0
    bridgeWeight = 0
    onBridge = 0
    time = 0
    
    while front < truckCnt:
        if truckStart and truckStart[front] + bridge_length == time:
            bridgeWeight -= truck_weights[front]
            onBridge -= 1
            front += 1
            
        if end < truckCnt and truck_weights[end] + bridgeWeight <= weight and onBridge < bridge_length:
            bridgeWeight += truck_weights[end]
            truckStart.append(time)
            end += 1
            onBridge += 1
        
        time += 1
    
    return time