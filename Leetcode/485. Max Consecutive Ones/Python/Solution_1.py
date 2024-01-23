class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        solution = 0
        tmp = 0

        for n in nums:
            if n == 1:
                tmp += 1
            else:
                if tmp > solution:
                    solution = tmp
                tmp = 0
        
        return tmp if tmp > solution else solution