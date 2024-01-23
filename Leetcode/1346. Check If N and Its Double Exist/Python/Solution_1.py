class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for n in arr:
            if n * 2 in arr and n != 0:
                return True
            elif n == 0:
                zeroes = arr.count(n)
                if zeroes > 1:
                    return True

        return False