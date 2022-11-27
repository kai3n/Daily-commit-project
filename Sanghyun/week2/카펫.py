
def solution(brown, yellow):
    # 가로길이와 세로길이 저장 
    answer=[]
    # 격자 총 갯수
    total = brown + yellow
    for x in range(1,total+1):
        # 일단 나올수있는 경우의수 약수로 구함 
        if total%x == 0:
            y = int(total/x) 
            # 가로가 세로보다 크거나 같음 
            if x >= y:
                # 갈색 격자는 노란색 격자의 가로 *2 + 세로 *2 -4 되야 되므로 이 조건 맞는 x,y값 리스트에 추가 
                if x*2 + y*2 == brown +4:
                    answer.append(x)
                    answer.append(y)
    # 카펫의 총 가로 길이 세로길이 반환 
    return answer