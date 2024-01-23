class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0

        for i in operations:
            if "-" in i:
                result -= 1
            else:
                result += 1
        
        return result