class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        solution = []
        n = len(nums) * 2

        for i in range(n):
            solution.append(nums[i%len(nums)])
        
        return solution