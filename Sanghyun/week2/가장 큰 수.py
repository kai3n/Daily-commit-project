def solution(numbers):
    # numbers 리스트에 int형을 전부 str으로 바꾼뒤 list로 변환 
    str_number = list(map(str,numbers))
    # 최대 1000자리수 까지 가능 하므로 문자열 *3 해서 정렬 후 내림차수 
    str_number.sort(key = lambda x : x*3,reverse = True)
    # 리스트 합쳐서 문자열 int형으로 변환 그 이유는 0000 <<이런 값일수도 있기떄문에 int변환 후 다시 str 변화해서 리턴
    return str(int(''.join(str_number)))