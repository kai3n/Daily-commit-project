# 기울기 구하는 함수
def gradient(a, b):
    return (a[1]-b[1])/(a[0]-b[0])

def solution(dots):
    answer = 0
    # 기울기가 같으면 평행이므로 1로 갱신
    if gradient(dots[0], dots[1]) == gradient(dots[2], dots[3]) or gradient(dots[0], dots[2]) == gradient(dots[1], dots[3]) or gradient(dots[0], dots[3]) == gradient(dots[1], dots[2]):
        answer = 1
    # 평행이면 1 반환 아니면 0반환
    return answer
