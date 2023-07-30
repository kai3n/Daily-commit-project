def solution(numlist, n):
    # n이랑 가까운 순서대로 정렬 값 반환
    return sorted(numlist, key=lambda x: (abs(n-x), -x))