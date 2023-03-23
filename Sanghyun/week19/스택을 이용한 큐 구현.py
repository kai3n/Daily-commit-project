class MyQueue:
    # input, output 초기화 
    def __init__(self):
        self.input = []
        self.output = []

    # input에 추가
    def push(self, x):
        self.input.append(x)
        
    #output 정렬 시킨 후 output에서 pop()
    def pop(self): 
        self.peek()
        return self.output.pop()
    
    # output이 없으면 input을 역순으로 저장
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    # 비어있는거 확인 후 Ture, False 반환
    def empty(self):
        return self.input == [] and self.output == []