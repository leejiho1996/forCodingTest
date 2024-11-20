def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    dic = {"next": 10, "prev": -10}
    
    # 전체 비디오 길이 초 단위로 변경
    end_min, end_sec = video_len.split(":")
    end_total = int(end_min) * 60 + int(end_sec)
    
    # op_start, op_end 초 단위로 변경
    op_start_min, op_start_sec = op_start.split(":")
    op_end_min, op_end_sec = op_end.split(":")
    
    op_start_total = int(op_start_min) * 60 + int(op_start_sec)
    op_end_total = int(op_end_min) * 60 + int(op_end_sec)
    
    # pos 초 단위로 변경
    pos_min, pos_sec = pos.split(":")
    pos_total = int(pos_min) * 60 + int(pos_sec)
    
    if op_start_total <= pos_total < op_end_total:
            pos_total = op_end_total
            
    for i in commands:
        pos_total += dic[i]
        pos_total = max(0, pos_total) # 0보다 작아지면 0이 되게 함
        pos_total = min(end_total, pos_total) # 비디오 길이보다 길어지면 비디오 길이가 되게 함
        
        if op_start_total <= pos_total < op_end_total:
            pos_total = op_end_total
        
    if pos_total // 60 < 10:
        answer += "0" + str(pos_total // 60)
    else:
        answer += str(pos_total // 60)
    
    answer += ":"
    
    if pos_total % 60 < 10:
        answer += "0" + str(pos_total % 60)
    else:
        answer += str(pos_total % 60)
    
    # answer += str(pos_total // 60)
    # answer += ":"
    # answer += str(pos_total % 60)
    
    return answer