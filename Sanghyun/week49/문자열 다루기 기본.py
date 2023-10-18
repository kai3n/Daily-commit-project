def solution(s):
      # 숫자로만 되어있고, 길이가 4,6이면 True 반환, 아니면 False반환
      return s.isdigit() and len(s) in [4,6]