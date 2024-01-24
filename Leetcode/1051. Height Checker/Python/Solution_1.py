class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        solution = 0
        
        for x, y in zip(heights, sorted_heights):
            if x != y:
                solution += 1
        
        return solution