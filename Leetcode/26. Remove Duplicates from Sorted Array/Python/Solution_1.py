class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        last = nums[0]
        
        for n in nums[1:]:
            if n != last:
                nums[index] = last = n
                index += 1

        return index