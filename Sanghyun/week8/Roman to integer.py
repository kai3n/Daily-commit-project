class Solution:
    def romanToInt(self, s: str) -> int:
        # 로마 문자에 대한 값 저장
        li = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        # 결과값 반환
        answer = 0 
        # I가 제일 작은 값이므로 비교기위해서 저장
        first = 'I'
        # 4 9 가 나올경우 대비해서 미리 뒤집어서 반복
        for value in s[::-1]:
            # li에 값보다 더 큰데 먼저 나왔으면 그 값만큼 마이너스 후 갱신 
            if li[value] < li[first]:
                answer = answer - li[value]
            # 먼저 안 나왔으면 일반적인 경우이므로 플러스 후 갱신
            else:
                answer = answer + li[value]
            # first를 갱신 시켜줌 
            first = value
        # 로마 숫자 값을 반환
        return answer
