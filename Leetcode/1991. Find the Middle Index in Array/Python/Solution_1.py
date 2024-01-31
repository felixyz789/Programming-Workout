class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        total = 0
        for n in nums:
            total += n
        
        current = 0
        for i,n in enumerate(nums):
            right = total - current - n
            if current == right:
                return i
            current += n
        
        return -1