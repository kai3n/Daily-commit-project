# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        for i in range(k):
            street.closeDoor()
            street.moveLeft()
        res = 0
        while not street.isDoorOpen():
            street.openDoor()
            res += 1
            street.moveLeft()
        return res
