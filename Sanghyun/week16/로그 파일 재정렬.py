from typing import List
class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 숫자 로그, 문자 로그 저장공간 
        digit , letter = [], [] 
        for log in logs :
            # 식별자 제외하고 숫자인지 문자인지 파별
            if log.split()[1].isdigit():
                digit.append(log)
            else :
                letter.append(log)
        
        # 문자로그로 먼저 정렬한뒤 2차로 식별자를 기준으로 정렬
        letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))
        # 숫자는 정렬이 필요 없으므로 리스트 더한후 값 반환 
        return letter + digit