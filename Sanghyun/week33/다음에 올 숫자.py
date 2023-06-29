def solution(common):
    answer = 0
    # 등비수열 등차수열 판단
    if (common[1]-common[0]) != (common[2] - common[1]):
        # 등비수열일 경우 마지막값 다음값 계산
        answer = common[-1] * (common[1] / common[0])
    else:
        # 등차수열일 경우 마지막값 다음값 계산
        answer = common[-1] + common[1] - common[0]
    # 등차수열 등비수열인지 판단하고 마지막값 다음값 반환
    return answer