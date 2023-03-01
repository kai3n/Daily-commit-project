class MyCalendar:

    def __init__(self):
        # 예약된 리스트 저장
        self.booked = [] 
        
    def book(self, start: int, end: int) -> bool:
        # 저장된 start , end 뽑아내기 
        for s,e in self.booked:
            #  start가 리스트의 값 중간이면 False 반환
            if s<= start < e:
                return False
            # end가 리스트의 값 중간이면 False반환
            elif s< end <=e:
                return False
            # start, end가 값을 벗어날 경우 False반환
            elif start <= s and e < end :
                return False
        # 리스트에 저장 
        self.booked.append([start,end])
        # 위 경우가 아니라면 예약가능하므로 True반환
        return True