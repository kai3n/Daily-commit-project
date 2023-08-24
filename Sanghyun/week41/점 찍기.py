def solution(k, d):
    answer = 0
    for x in range(0,d+1,k):
        # x 좌표를 돌면서 y좌표 값 찾기
        res = int((d**2 - x**2)**0.5)
        # y 좌표에 몇개의 값이 찍히는지 값 저장
        answer += (res // k) + 1        
    # d거리 안에 몇개의 점이 찍히는지 반환
    return answer