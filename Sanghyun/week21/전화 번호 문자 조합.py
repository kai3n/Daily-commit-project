from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # digits개수 맞을때 까지 계속 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                # 입력값 자리수 갱신 하면서 탐색
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 문자 digits 없을때 빈 값 반환
        if not digits:
            return []
        # 전화 번호를 키로 문자 값 저장
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result