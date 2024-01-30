class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        nums_map = Counter(deck)
        result = math.gcd(*nums_map.values())
        return result > 1