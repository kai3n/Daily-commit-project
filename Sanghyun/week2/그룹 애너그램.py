from typing import List 
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 존재 않는 키 값 에러 방지하기 위해서 defaultdict으로 선언 
        anagrams = collections.defaultdict(list)
        
        for word in strs :
            # 키 값이 없으면 []로 채워짐 키값있으면 list에 계속추가 
            anagrams[''.join(sorted(word))].append(word)
        
        # 딕셔너리 값들만 리스트로 변환 후 출력
        return list(anagrams.values())
        