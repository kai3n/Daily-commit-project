def solution(s):
    # 결과 저장 
    answer = ''
    # s문자열을 전부 소문자로 바꾸고 공백기준으로 리스트로 변호나 
    s_to_list = s.lower().split(" ")
    # 리스트 하나씩 반복
    for item in s_to_list:
        # 맨 앞 문자가 공백일때 처리 
        if item =="":
            answer += " "
        # 맨앞 문자가 알파벳일떄 첫글자만 대문자 나머지 소문자로 저장
        elif item[0].isalpha() ==True:
            answer +=" "+item[0].upper() + item[1:]
        # 맨 앞문자가 앞파벳이 아니면 그냥 다 저장 
        else:
            answer +=" "+item
    # 맨앞에 공백문자 처리 한후 반환 
    return answer.lstrip()