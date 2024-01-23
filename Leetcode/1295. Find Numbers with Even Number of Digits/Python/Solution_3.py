class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        solution = 0

        for n in nums:
            solution += 1 - len(str(n))&1
            
        return solution 