class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        solution = []

        for i in range(1,len(mountain)-1):
            if mountain[i]>mountain[i+1] and  mountain[i]>mountain[i-1]:
                solution.append(i)
        
        return solution