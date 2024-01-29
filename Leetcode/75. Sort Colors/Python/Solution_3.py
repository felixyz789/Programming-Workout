class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, len(nums) - 1
        i = 0       

        def swap(a,b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp
        
        while i <= right:
            if nums[i] == 0:
                swap(i,left)
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(i,right)
                right -= 1