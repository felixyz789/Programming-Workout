class Solution(object):
    def sortedSquares(self, nums):
        result = [0] * len(nums)
        counter = len(nums)-1
        
        upper = len(nums)-1
        down = 0     

        while counter >= 0:
            if nums[upper]*nums[upper] >= nums[down]*nums[down]:
                result[counter] = nums[upper] * nums[upper] 
                upper -= 1
                counter -= 1
            else:
                result[counter] = nums[down] * nums[down]
                down += 1
                counter -= 1
        return result