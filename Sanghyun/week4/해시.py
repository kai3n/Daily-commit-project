def solution(phone_book):
    # 초기 값 갱신 
    answer = True
    # 해시 저장 변수 
    hash_map = {}
    # phone_number 키값으로 다 저장
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        # 문자 하나씩 저장하기 위한 변수
        temp = ""
        for number in phone_number:
            # 문자을 계속 갱신해줌
            temp += number
            # temp가 hash_map에 있고 phone_number랑 다르면 접두어이므로 False반환 
            if temp in hash_map and temp != phone_number:
                answer = False
    # 위 조건이 안맞으면 접두어 없으므로 true반환 
    return answer