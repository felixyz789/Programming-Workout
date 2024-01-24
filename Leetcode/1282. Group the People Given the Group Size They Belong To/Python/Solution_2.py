class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_map = defaultdict(list)
        solution = []
        
        for i in range(len(groupSizes)):
            groups_map[groupSizes[i]].append(i)
            if len(groups_map[groupSizes[i]]) % groupSizes[i] == 0:
                solution.append(groups_map[groupSizes[i]][-groupSizes[i]:])

        return solution