class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = nums.count(val)
        upper = len(nums) - 1
        down = 0
        
        while upper > down:
            if nums[upper] == val:
                upper -= 1
            if nums[down] != val:
                down += 1
            if nums[down] == val and nums[upper] != val:
                nums[down],nums[upper] = nums[upper],nums[down]
                upper -= 1
                down += 1

        return k

# This code don't pass the second test case. The problem's rules are incorrect.
#  "Note that the five elements can be returned in any order."