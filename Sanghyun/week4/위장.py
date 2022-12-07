def solution(clothes):
    clothes_type = {}
    # 몇개의 경우의 수가 나오는지 저장
    count = 1
    # clothes 수 만큼 반복 
    for name, category in clothes:
        # category가 clothes_type에 없을때  초기값 2로 설정, 해당 종류의 의상이 없을때랑 잇을때 두가지가 생김
        if category not in clothes_type:
            clothes_type[category] = 2
        # 존재하면 +1 추가 
        else:
            clothes_type[category] += 1
    # clothes_type 있는 값들을 리스트로 다 반환 
    for num in clothes_type.values():
        # 전체 다 곱하면 총 나올수 있는 경우의수
        count *= num
    # 의상을 하나도 안입는 경우 뺴서 반환
    return count - 1