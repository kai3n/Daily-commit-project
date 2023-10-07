str = input()

answer = ''
for c in str:
    # 대문자일경우 소문자로 해서 저장
    if c.isupper() is True:
        answer +=c.lower()
    else:
        # 대문자로 저장
        answer +=c.upper()
# 대소문자 바꿔서 출력
print(answer)
        