class ProductOfNumbers:

    def __init__(self):
        self.num = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.num = [1]
        else:
            self.num.append(self.num[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.num):
            return 0
        return self.num[-1] // self.num[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
