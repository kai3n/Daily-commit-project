from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 병합 후 담을 리스트
        merged = []
        # intervals에서 0인덱스 기준으로 정렬
        for i in sorted(intervals,key = lambda x:x[0]):
            # merged 두번째 인덱스와 i의 첫번째 인덱스 비교 후 값갱신 
            if merged and i[0] <=merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],i[1])
            else:
                # 위조건에 안맞으면 구간이 다르므로 merged에 추가
                merged += [i]
        # 구간 병합된 리스트 반환
        return merged
                