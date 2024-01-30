class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0

        for i,n in enumerate(plants[:-1]):
            steps += 1
            water -= n
            if water < plants[i+1]:
                steps += (i + 1) * 2
                water = capacity
        
        return steps + 1