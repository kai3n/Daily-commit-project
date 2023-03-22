import collections
# 스택 구현 
class MyStack:
    # 데크로 초기화
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞으로 정렬시킴 
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    # 위에서 정렬시키므로 popleft로 뽑으면 됨
    def pop(self):
        return self.q.popleft()
    # q[0]가 젤 위 값
    def top(self):
        return self.q[0]
    # 비어있으면 True 아니면 False
    def empty(self):
        return len(self.q) == 0