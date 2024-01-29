class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        house = defaultdict(int)
        result = 0
        
        full_trip = 0 
        for t in travel:
            full_trip += t
        
        travel_done = len(travel) - 1
        for s in garbage[::-1]:
            if "G" in s:
                if "G" in house:
                    house["G"] += s.count("G")
                else: 
                    house["G"] = s.count("G")
                    result += full_trip
            if "P" in s:
                if "P" in house:
                    house["P"] += s.count("P")
                else: 
                    house["P"] = s.count("P")
                    result += full_trip
            if "M" in s:
                if "M" in house:
                    house["M"] += s.count("M")
                else: 
                    house["M"] = s.count("M")
                    result += full_trip
            
            full_trip -= travel[travel_done]
            travel_done -= 1

        for k in house:
            result += house[k]

        return result