def solution(s):
    # index초과때문에 맨앞에 0값 넣어줌
    temp = [0,s[0]]

    for i in s[1:]:
        # s문자랑 temp마지막 문자랑 같으면 pop해서 문자 제거 다르면 temp에 저장
        if temp[-1]!=i:
            temp.append(i)
        else:
            temp.pop()
    # temp에 0값만 남아있으면 다 짝지어지므로 1반환 아니면 0반환
    return 1 if len(temp)==1 else 0