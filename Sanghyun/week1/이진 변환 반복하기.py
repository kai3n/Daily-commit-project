def solution(s):
    # 이진 변환 몇번 반복하는지 저장
    num = 0
    # 0 개수 저장
    zero_count = 0
    # s 가 1이 아닐떄 까지 반복
    while s != '1':
        # s에 0 개수 카운트 
        zero_count += s.count('0')
        # s에 0을 다 제거 한 길이
        length = len(s.replace('0',''))
        # 0을 제거한 길이를 이진 변환하기 
        s = bin(length)[2:]
        # 이진변환 반복 횟수
        num +=1
    # 이진변환 반복횟수, 0을 몇개 제거햇는지 갯수 리스트로 반환 
    return [num,zero_count]