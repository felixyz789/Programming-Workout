class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_map = defaultdict(int)
        maximum = nums[0]

        for n in nums:
            nums_map[n] += 1
            maximum = max(n, maximum)

        solution = maximum

        while k > 0:
            if maximum in nums_map:
                k -= nums_map[maximum]
                solution = maximum
            maximum -= 1
        
        return solution