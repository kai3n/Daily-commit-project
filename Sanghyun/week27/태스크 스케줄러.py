import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 태스크 카운터
        counter = collections.Counter(tasks)

        result = 0

        while True:
            # 몇개 빠지는지 체크
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                # counter에서 task 요소 빼기
                counter.subtract(task)
                # 0 이하 값은 counter 목록에서 제거
                counter += collections.Counter()
            # counter가 없으면 종료 
            if not counter:
                break
            # 태스크 실행하기 위한 간격 갱신
            result += n - sub_count + 1
        # 태스크 실행하기 위한 간격 반환
        return result