def solution(my_string, queries):
    for start, end in queries:
        # 뒤집을부분만 [::-1]로 뒤집어주고 나머지 문자열 다 더해줌
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    # 다 뒤집힌 문자열 반환
    return my_string