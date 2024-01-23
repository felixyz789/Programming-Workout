class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        x = pref[0]

        for i in range(1,len(pref)):
            arr.append(x^pref[i])
            x ^= arr[-1]
            
        return arr