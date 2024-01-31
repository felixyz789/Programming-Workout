class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        solution = []

        while left < right and top < bottom:
            for i in range(left, right):
                solution.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                solution.append(matrix[i][right - 1])
            right -= 1

            if left == right or top == bottom:
                return solution

            for i in range(right - 1, left - 1, -1):
                solution.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                solution.append(matrix[i][left])
            left += 1

        return solution
