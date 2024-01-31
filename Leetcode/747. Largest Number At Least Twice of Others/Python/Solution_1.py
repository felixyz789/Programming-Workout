class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = max(nums)
        count = 0
        count2 = 0
        solution = "hey"
        
        for i,n in enumerate(nums):
            if n == maximum:
                if count + 1 == 2:
                    return -1
                count += 1
                solution = i
                
            elif n*2 > maximum:
                return -1
        
        return solution
            