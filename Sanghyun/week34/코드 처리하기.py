def solution(code):
    # 반환할 값 
    ret = ''
    # 0, 1 모드 
    mode = 0 
    # code 인덱스,값 출
    for idx,value in enumerate(code):
        # mode 변경
        if value == '1' and mode == 0 :
            mode = 1
        elif value =='1' and mode ==1:
            mode = 0
        # mode가 0이고 인덱스가 짝수이면 값 저장
        elif idx %2==0 and mode ==0:
            ret += value
        # mode가 1이고 인덱스가 홀수이면 값저장 
        elif idx%2==1 and mode ==1:
            ret += value
    # 반환값이 없으면 EMPTY 반환
    if len(ret)==0:
        return 'EMPTY'
    # 조건에 맞게 저장 후 반환
    return ret