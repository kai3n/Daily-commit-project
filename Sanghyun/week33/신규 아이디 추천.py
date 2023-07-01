import re

def solution(new_id):
    # 소문자로 치환
    new_id=new_id.lower()
    # 정규표현식 이용해서 알파벳,숫자,-,_,.빼고 다 제외시키기
    lvl2 = re.compile('[0-9a-z_.\-]+')
    answer = lvl2.findall(new_id)
    answer = ''.join(answer)
    # 마침표가 연속으로 나오면 .로 변경
    while '..' in answer:
        answer = answer.replace('..','.')
    # 양쪽끝에 마침표로 끝나면 제거
    answer = answer.strip('.')
    # 빈 문자열이면 a대입
    if len(answer) ==0:
        answer = 'a'
    # 길이가 16이상이면 첫 15개의 문자만 사용 마지막이 마침표라면 제거
    if len(answer)>=16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    # 길이가 2이하라면 마지막문자 길이가 3이 될때까지 더해줌
    if len(answer)<=2:
        size = len(answer)
        while size<3:
            answer+=answer[-1]
            size = len(answer)
    # 새로운 아이디 추천한 값 반환
    return answer