class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] in numbers_dict:
                return[i, numbers_dict[target - nums[i]]]
            numbers_dict[nums[i]] = i