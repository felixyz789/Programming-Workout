class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        missing = []

        for n in range(1, len(nums) + 1):
            if n not in set_nums:
                missing.append(n)
        
        return missing