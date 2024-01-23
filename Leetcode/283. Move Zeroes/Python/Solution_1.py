class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):            
            left_n = nums[l] 
            right_n = nums[r]
            if left_n == 0 and right_n != 0:
                nums[l] , nums[r] = nums[r] ,nums[l]
                l += 1
            elif left_n != 0:
                l += 1