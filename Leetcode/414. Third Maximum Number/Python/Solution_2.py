class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = sorted(set(nums),reverse = True)
        return nums_set[2] if len(nums_set) > 2 else nums_set[0]