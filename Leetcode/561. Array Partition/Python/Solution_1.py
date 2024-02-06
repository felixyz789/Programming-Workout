class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        solution = 0
        for i in range(0,len(nums),+2):
            solution += min(nums[i], nums[i + 1])
        return solution