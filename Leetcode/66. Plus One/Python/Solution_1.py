class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        all_nine = True
        index = len(digits) - 1
        len_digits = len(digits) - 1
        
        for i,n in enumerate(digits[::-1]):
            if n == 9:
                index -= 1
                digits[len_digits - i] = 0
            else:
                all_nine = False
                break

        if all_nine:
            for i in range(1,len(digits)):
                digits[i] = 0
            digits[0] = 1
            digits.append(0)
            return digits

        digits[index] = digits[index] + 1 
        return digits