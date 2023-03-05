from typing import List 
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict는 에러 방지하기 위해서 사용
        dict = collections.defaultdict(list)
        
        for item in strs :
            # 정렬시켜서 키값이 있을시 값추가
            dict[''.join(sorted(item))].append(item)
        
        # 값들만 리스트로 반환
        return list(dict.values())
