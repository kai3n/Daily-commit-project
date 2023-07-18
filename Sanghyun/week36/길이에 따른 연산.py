from math import prod
def solution(num_list):
    # 길이가 11이상이면 다 더하고 이하면 다 곱한값 반환
    return sum(num_list) if len(num_list)>=11 else prod(num_list)