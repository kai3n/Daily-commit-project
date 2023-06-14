def solution(ingredient):
    temp = []
    # 햄버거 개수
    count = 0
    for i in ingredient:
        # 재료를 계속 저장
        temp.append(i)
        # 재료들이 1231로 있으면 햄버거를 하나 만들수 있으므로 햄버거 개수 갱신
        if temp[-4:] == [1, 2, 3, 1]:
            count += 1
            # 만들어진 재료는 temp에서 제거
            for _ in range(4):
                temp.pop()
    # 햄버거 개수 반환
    return count