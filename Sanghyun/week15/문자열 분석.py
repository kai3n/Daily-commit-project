import sys

while True:
    # 문자열 입력받음
    strings = sys.stdin.readline().rstrip('\n')
    # 대문자, 소문자, 공백, 숫자가 몇개씩 인지 갱신하기 위해서 저장
    upper, lower, space, num = 0, 0, 0, 0
    # 문자열 입력이 없을때는 반복문 탈출
    if not strings:
        break
    for item in strings:
        # 대문자 검사
        if item.isupper():	
            upper += 1
        # 소문자 검사
        elif item.islower():
            lower += 1
        # 숫자 검사
        elif item.isdigit():
            num += 1
        # 공백 검사
        elif item.isspace():
            space += 1
    # 출력
    sys.stdout.write("{} {} {} {}\n".format(lower, upper, num, space))