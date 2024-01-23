class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        
        for n in range(len(nums)):
            for m in range(n + 1, len(nums)):
                if nums[n] == nums[m]:    
                    result += 1
                    
        return result