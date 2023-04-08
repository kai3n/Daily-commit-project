from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 부분 집합 저장
        result = []

        def dfs(index, path):
            # 부분집합 추가
            result.append(path)

            # 경로를 만들면서 DFS로 탐색
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        # 부분 집합 반환
        return result