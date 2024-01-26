class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0

        for i in range(len(nums)):
            l = nums[i]
            if l != val and nums[r] == val:
                nums[r], nums[i] = nums[i], nums[r] 
                r += 1
            elif nums[r] != val:
                r += 1
        
        return r 