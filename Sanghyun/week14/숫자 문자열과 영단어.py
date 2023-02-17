def solution(s):
    # 변환할 문자 다 저장 
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    # 딕셔너리 개수만큼 반복 
    for key, value in num_dic.items():
        # answer값 다 replace로 대체 
        answer = answer.replace(key, value)
    # 결과값 정수형으로 반환
    return int(answer)