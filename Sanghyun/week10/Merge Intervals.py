from typing import List

class Solution:
    # 구간 겹치는 곳 병합 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 병합되면 반환하는 리스트 
        merged = []
        # interval에서 첫번째를 기준으로 정렬해서 반복 
        for i in sorted(intervals,key = lambda x:x[0]):
            # merged에 값이 있고 i 0번쨰 인덱스가 merged의 마지막 1번쨰 인덱스보다 작을때 값을 갱신 
            if merged and i[0] <=merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],i[1])
            else:
                # 만약에 merged가 없거나 i 0번쨰 인덱스가 merged의 마지막 1번쨰 인덱스보다 클때 그냥 merged에 리스트로 추가 
                merged += [i]
        # 병합 한 리스트 반환 
        return merged