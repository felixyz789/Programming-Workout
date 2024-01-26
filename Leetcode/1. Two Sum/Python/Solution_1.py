class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = {}

        for i,n in enumerate(nums):
            if target - n in number_dict:
                return[i,number_dict[target - n]]
            else:
                number_dict[n] = i