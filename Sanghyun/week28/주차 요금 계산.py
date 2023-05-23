from collections import defaultdict
import math

def solution(fees, records):
    # 결과값 저장 
    result = []
    # 주자 차량 관리 
    parking = defaultdict(int)
    # 주차 차량 요금관리 
    parking_fee = defaultdict(int)

    for record in records:
        # record에서 필요한 값 추출
        time, car_num, check = record.split()
        hour, minute = time.split(":")
        total_minute = int(hour) * 60 + int(minute)
        # 차가 주차될떄 시간 계산
        if check == "IN":
            parking[car_num] = total_minute
        # 차가 나갈때 시간 계산
        else:
            parking_fee[car_num] += total_minute - parking[car_num]
            # 차가 나가면 주차장에서 삭제 
            del parking[car_num]
    # 하루가 지나도 안나갔을때 주차시간 계산
    for car, minute in parking.items():
        parking_fee[car] += 23 * 60 + 59 - minute
    # 주차 요금 계산후 차량번호순으로 얼마인지 계산
    for item in sorted(list(parking_fee.items())):
        price = int(fees[1] + math.ceil((item[1] - fees[0]) / fees[2]) * fees[3])
        if price >= fees[1]:
            result.append(price)
        else:
            result.append(fees[1])
    # 차번호 별로 주차요금 반환
    return result