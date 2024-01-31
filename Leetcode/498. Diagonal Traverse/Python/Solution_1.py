class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        nums = [[] for _ in range(n + m - 1)]
        for i in range(m):
            for j in range(n):
                nums[i+j].append(mat[i][j])

        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.extend(nums[i][::-1])
            else:
                ans.extend(nums[i])
        
        return ans