from typing import List
class Solution:
    # 두 배열 교집합 반환 
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 중복 제거를 위해서 set사용 
        result = set()
        # nums1, nums2 정렬 
        nums1.sort()
        nums2.sort()
        # nums1,nums2 인덱스 설정 
        i = j = 0 
        # 인덱스들이 초과 안했을때 반복 
        while i < len(nums1) and j < len(nums2):
            # nums1[i]값이 더 크면 j인덱스를 올려서 다시비교 
            if nums1[i]>nums2[j]:
                j+=1
            # nums2[j]값이 더 크면 i인덱스를 올려서 다시비교
            elif nums1[i]<nums2[j]:
                i+=1
            # 위 두경우가 아니면 교집합이므로 result에 삽입후 i, j 인덱스 갱신 
            else:
                result.add(nums1[i])
                i+=1
                j+=1
        # 두 배열 교집합 반환 
        return result