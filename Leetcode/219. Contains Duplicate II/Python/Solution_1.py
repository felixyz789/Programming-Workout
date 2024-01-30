class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = defaultdict(list)

        for i,n in enumerate(nums):
            if n in num_dict and abs(i - num_dict[n]) <= k:
                return True
            num_dict[n] = i
        return False
