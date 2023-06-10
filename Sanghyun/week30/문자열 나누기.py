def solution(s):
    answer = 0
    # 나온 횟수 저장
    cnt1,cnt2=0,0
    for item in s:
        # 두 수가 같으면 분리하므로 answer 갱신
        if cnt1 == cnt2:
            answer +=1
            # 초기 비교할 값 저장
            temp = item 
        # 비교할값이랑 다르면 cnt2 갱신
        if temp != item:
            cnt2+=1
        # 비교할값이랑 같으면 cnt1 갱신
        else:
            cnt1+=1
    # 몇개 문자열로 분리할수 있는지 반환
    return answer