def solution(s):
    # 각 단위마다 문자열 길이저장
    result=[]
    # 문자가 하나면 1반환
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1):
        # 문자저장
        b = ''
        # 반복되는 카운터 저장
        count = 1
        # 초기 문자 저장
        temp=s[:i]

        for j in range(i, len(s)+i, i):
            # 이전문자랑 같으면 count 갱신
            if temp==s[j:i+j]:
                count+=1
            else:
                # 문자 반복이 있을때 없을때 따라서 문자저장
                if count!=1:
                    b += str(count)+temp
                else:
                    b += temp
                # 비교할 문자 갱신
                temp=s[j:j+i]
                # 반복되는 카운터 초기화
                count = 1
        # 문자 길이 단위마다 결과값에 저장
        result.append(len(b))
    # 문자 길이가 최소인값 반환
    return min(result)