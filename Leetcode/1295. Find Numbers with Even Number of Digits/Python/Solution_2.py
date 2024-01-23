class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        return len([x for x in nums if not len(str(x)) & 1])

    # this code is quite the same of the solution 1

    #Reference : bitwise operator | https://www.prepbytes.com/blog/python/and-operator-in-python/