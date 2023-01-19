from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 투 포인트 형식으로 0으로, blue는 배열의 길이 선언 
        red, white, blue = 0, 0, len(nums)

        # 블루가 제일 크므로 white가 blue보다 작으면 계속 반복 
        while white < blue:
            # white보다 작다면 red이므로 값 갱신 
            if nums[white] < 1:
                nums[red],nums[white] = nums[white], nums[red]
                # 갱신후 인덱스 갱신 
                white +=1
                red +=1
            # 1보다 크면 blue이므로 
            elif nums[white] >1:
                # blue 인덱스 갱신 
                blue -=1
                # blue 값 갱신 
                nums[white],nums[blue] = nums[blue], nums[white]
            else:
                # 값이 1이므로 white값만 갱신 
                white +=1