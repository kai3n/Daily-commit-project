import sys
# 시간복잡도 초과해서 Counter사용 
from collections import Counter 

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
# Counter에 저장 
counter = Counter(nums) # 
stack = [0]

result = [-1] * n

for i in range(1, n):
    # 인덱스를 통해 오등큰수가 있는지 확인
    while stack and counter[nums[stack[-1]]] < counter[nums[i]]:
        # 오등큰수일때 stack에서 값을 뽑아내고 오등큰수를 저장
        result[stack.pop()] = nums[i]

    # 오등큰수를 비교할 인덱스를 추가
    stack.append(i)
print(result)
