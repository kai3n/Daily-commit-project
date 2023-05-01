from typing import List


class Solution:
    # nums에서 target 인덱스 출력 후 반환 없으면 -1반환
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1