class Solution(object):
    def sortedSquares(self, nums):
        solution = [0] * len(nums) 
        l = 0
        r = len(nums) - 1
        counter = len(nums) - 1
        
        while r >= l:
            if nums[l] ** 2 >= nums[r] ** 2:
                solution[counter] = nums[l] ** 2
                l += 1
                counter -= 1
            else:
                solution[counter] = nums[r] ** 2
                r -= 1
                counter -= 1

        return solution

# At the end of array 101 module i find this problem that i have solved in the past and i decided to do it again.
# Quite similar but the while condition change