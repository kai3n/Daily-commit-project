from collections import deque

def solution(cacheSize, cities):
    time = 0
    # 맨앞에서 뺼수있게 데큐선언 
    buffer = deque()
    # cacheSize가 0일떄는 항상 miss이므로 도시 개수*5해서 반환 
    if cacheSize == 0 :
        return len(cities)*5
    else:
        # cacheSize가 0이 아니고 도시 리스트 수만큼 반복
        for v in cities:
            # 대소문자 구별 안하므로 소문자로 변환 
            city = v.lower()
            # 캐시 저장 공간에 도시가 잇으면 1초 걸리므로 갱신 
            if city in buffer:
                time +=1
            # 캐시 저장 공간에 도시가 없으면 5초 걸리므로 갱신 
            else:
                time +=5
            # city가 캐시 저장공간에 잇으면 사용하므로 buffer에서 제거
            if city in buffer:
                buffer.remove(city)
            # city가 캐시 저장공간에 없고 buffer크기가 cacheSize보다 크다면 제일 사용 안하는 city를 pop시킨다
            else:
                if cacheSize<=len(buffer):
                    buffer.popleft()
            # buffer에 city 저장 
            buffer.append(city)
    # 총 실행시간 반환 
    return time