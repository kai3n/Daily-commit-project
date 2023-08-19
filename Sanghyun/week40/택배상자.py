def solution(order):
    #보조 컨테이너 벨트 저장
    sub_store = []
    # 인덱스
    idx = 1
    # 상자를 몇개 실을수 있는지 저장
    count = 0 
    # idx가 order랑 같을때까지 반복
    while idx != len(order)+1:
        # 보조 컨테이너 벨트에 저장
        sub_store.append(idx)
        # 보조 컨테이너 벨트 마지막 값과 메인 컨테이너 벨스 값이 같으면 상자에 실고 보조 컨테이너 벨트에서 제거
        while sub_store and sub_store[-1] == order[count]:
            count+=1
            sub_store.pop()
        # 인덱스 갱신
        idx+=1
    # 택배상자를 몇개 실을수 있는지 반환
    return count