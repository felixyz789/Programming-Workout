class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minimum = nums[0]
        maximum = nums[0]

        for n in nums[1:]:
            if n > maximum:
                maximum = n
            elif n < minimum:
                minimum = n

        difference = (maximum - k) - (minimum + k)

        if difference <= 0:
            return 0

        return difference