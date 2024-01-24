class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        solution = nums[0]
        
        counter = 1
        for n in nums:
            if n != solution and counter != 3:
                solution = n
                counter += 1
        
        return solution if counter == 3 else nums[0] 