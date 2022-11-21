from typing import List
class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 숫자로그 , 문자로그 리스트 
        digit , letter = [], [] 
        for log in logs :
            # 인덱스 0 은 식별자 이므로 인덱스 1부터 숫자인지, 문자인지 판별 
            if log.split()[1].isdigit():
                digit.append(log)
            else :
                letter.append(log)
        
        # 문자열이 먼저 오기 때문에 초기 letter[1:] 기준으로 정렬 후 letter[0]기준으로 정렬한다 
        letter.sort(key=lambda x: (x.split()[1:],x.split()[0]))
        #숫자 로그는 입력 순서대로 하기때문에 정렬 안시켜도 됨 
        return letter + digit