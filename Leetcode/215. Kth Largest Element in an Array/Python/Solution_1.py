class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_map = defaultdict(int)
        maximum = nums[0]
        
        for n in nums:
            maximum = max(maximum,n)
            nums_map[n] += 1
        
        kth_element = maximum
        while k > 0:
            kth_element = maximum
            k -= nums_map[maximum]
            maximum -= 1
        
        return kth_element