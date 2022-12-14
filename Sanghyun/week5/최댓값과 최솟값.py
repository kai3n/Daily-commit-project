def solution(s):
    #문자열 공백 단위로 리스트로 변환후 리스트 값들을 int형으로 변환후 다시 리스트로 변환 
    answer =list(map(int,s.split(' ')))
    # answer을 오름차순으로 정렬 
    answer.sort()
    # 문자열로 최솟값과 최댓값 반환 
    return f"{answer[0]} {answer[-1]}"
    