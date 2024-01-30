class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        nums_map = defaultdict(int)

        for c in deck:
            nums_map[c] += 1

        all =  [nums_map[k] for k in nums_map]
        
        result = math.gcd(*all)

        return True if result > 1 else False        