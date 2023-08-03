def solution(my_string, overwrite_string, s):
    # 겹쳐쓸문자가 중간인지 체크 
    num = len(my_string) - len(overwrite_string) - s
    # 중간이라면 문자열 겹친거에 마지막 문자열도 다 저장 
    answer = my_string[:s] + overwrite_string + my_string[-num:] if num >0 else my_string[:s] + overwrite_string
    # 문자열 겹쳐써서 반환
    return answer