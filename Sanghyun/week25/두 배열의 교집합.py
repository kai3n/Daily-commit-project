from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        # 양쪽 다 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 갱신하면서 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            # 같을경우 result에 저장
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        # 교집합 반환
        return result