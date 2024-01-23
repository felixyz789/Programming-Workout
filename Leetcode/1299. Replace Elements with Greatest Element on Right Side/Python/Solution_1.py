class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        bigger = arr[-1]
        last = arr[-1]

        for i in range(len(arr) -2, -1, -1):
            last = arr[i]
            arr[i] = bigger
            if bigger < last:
                bigger = last 
        
        arr[-1] = -1
        
        return arr        