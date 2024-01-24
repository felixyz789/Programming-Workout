class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_map = defaultdict(list)

        for i in range(len(groupSizes)):
            groups_map[groupSizes[i]].append(i)
        
        solution = []

        for k in groups_map:
            for i in range(0, len(groups_map[k]), + k):
                solution.append(groups_map[k][i : i + k])
        
        return solution