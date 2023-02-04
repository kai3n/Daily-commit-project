from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Counter로 키 값에 따라 개수저장 
        counter = Counter(tasks)
        # 모든 태스크를 실행 하기 위한 최소 간격 저장 
        result = 0 

        while True:
            # counter에서 빠진 갯수 초기화 
            sub_count = 0
            # counter에서 값이 가장 흔한 것을 n+1개 만큼 추출 해서 반복 
            for task, _ in counter.most_common(n+1):
                # counter에서 task를 실행했다고 보고 값에서 1개 뺴기 
                counter.subtract(task)
                #최소 간격 갱신 
                result +=1
                # counter에서 빠진 갯수 갱신 
                sub_count +=1
                # 키값에 따른 값이 0이하는 필요없기 때문에 빈 Counter 객체를 더하면서 갱신 시켜주기 
                counter += Counter()
            # counter가 존재하지 않는다면 while문 탈출 
            if not counter:
                break 
            # 가장 흔한 것 반복 후 최소 간격 갱신 
            result += n - sub_count + 1
        # 태스크를 실행 하기 위한 최소 간경 반환 
        return result