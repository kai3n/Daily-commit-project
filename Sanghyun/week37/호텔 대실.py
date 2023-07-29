def solution(book_time):
    # 분으로 체크 
    time_table = [0 for _ in range(60 * 24)]
    # 시작시간 끝나는시간에 청소시간 저장
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10
        
        # 24시를 넘길경우 24시로 끝나는시간 저장
        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1
        # 대실하는 시간 체크 
        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    # 방을 가장많이 대실하고 있을때 값 출력
    return max(time_table)