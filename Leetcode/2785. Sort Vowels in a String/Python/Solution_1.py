class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        vowels_arr = [v for v in s if v in vowels]
        vowels_arr.sort()
        
        new_s = ""
        
        counter = 0
        for l in range(len(s)):
            if s[l] in vowels:
                new_s += vowels_arr[counter]
                counter += 1
            else: 
                new_s += s[l]
        
        return new_s