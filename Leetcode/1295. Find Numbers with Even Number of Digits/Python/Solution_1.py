class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        solution = 0

        for n in nums:
            if len(str(n)) % 2 == 0:
                solution += 1
                
        return solution 