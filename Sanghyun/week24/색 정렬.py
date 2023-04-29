from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 인덱스 저장
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            # red 이므로 값 갱신후 red, white 인덱스 갱신
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # blue 이므로 값 갱신 후 blue 인덱스 갱신
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            # white 인덱스만 갱신 
            else:
                white += 1
        