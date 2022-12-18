from collections import Counter

def solution(str1, str2):
    # 문자열 대소문자 구별안하기 때문에 소문자로 변환
    low_str1 = str1.lower()
    low_str2 = str2.lower()
    # 알파벳일때 담을 리스트 
    str1_list= []
    str2_list = []
    # str1에서 문자열 2개 단위로 알파벳 일 경우에만 list에 추가
    for i in range(len(str1)-1):
        if low_str1[i].isalpha() and low_str1[i+1].isalpha():
            str1_list.append(low_str1[i] + low_str1[i+1])
    # str2에서 문자열 2개 단위로 알파벳 일 경우에만 list에 추가
    for j in range(len(str2)-1):
        if low_str2[j].isalpha() and low_str2[j+1].isalpha():
            str2_list.append(low_str2[j] + low_str2[j+1])
    # Counter로 문자열 카운터 
    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)
    # counter1과 counter2 합집합의 요소들을 list에 변환 
    inter = list((counter1 & counter2).elements())
    # counter1과 counter2 교집합의 요소들을 list에 변환
    union = list((counter1 | counter2).elements())
    # 만약에 교집합과 합집합이 0이면 65536 반환 
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        # 자카드 유사도 계산 후 65536 곱해서 반환
        return int(len(inter) / len(union) * 65536)