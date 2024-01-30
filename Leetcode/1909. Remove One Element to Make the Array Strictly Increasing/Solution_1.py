class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        current = nums[0]
        count = []
        tmp = [current]
        for i,n in enumerate(nums[1:]):
            if n > current:
                tmp.append(n)
                current = n
            else:
                count.append(tmp)
                tmp = [n]
                current = n
        count.append(tmp)
        
        
        if len(count) == 1:
            return True
        if len(count) > 2:
            return False
        if len(count[0]) == 1 or len(count[1]) == 1:
            return True 
        if count[0][-2] < count[1][0] or count[0][-1] < count[1][1]:
            return True 
        
        return False