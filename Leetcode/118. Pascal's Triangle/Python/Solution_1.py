class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[] for _ in range(numRows)]

        for i in range(numRows):
            if i == 0:
                solution[i].append(1)
            else:
                for j in range(i + 1):
                    if j - 1 > -1 and j != i :
                        solution[i].append(solution[i - 1][j - 1] + solution[i - 1][j])
                    else:
                        solution[i].append(1)
        
        return solution