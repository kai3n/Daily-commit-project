class MyCircularQueue:
    # 배열을 원형큐 길이만큼 초기화, front , rear 포인트 초기화
    def __init__(self, k: int):
        self.q = [None] * k
        self.length = k
        self.front = 0
        self.rear = 0

    # rear None이면 비어있므로 값 할당후 rear 포인트 갱신
    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.lenth
            return True
        else:
            return False

    # front가 None이 아니면 값을 None으로 바꾸고 front 포인트 갱신
    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.length
            return True
    # front가 None이 아니면 해당 값 반환
    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]
    # rear -1 이 None이 아니면 해당 값 반환 
    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]
    # front rear이 같고 front가 None이면 비어있음
    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None
    # front rear이 같고 front가 None이 아니면 가득차있음
    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None