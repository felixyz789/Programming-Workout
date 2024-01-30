class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        def calc_distance(c,p):
            x = (c[0] - p[0]) * 1
            y = (c[1] - p[1]) * 1
            return sqrt(x * x + y * y)

        for c in queries:
            tmp = 0
            for p in points:
                distance = calc_distance(c, p)
                if distance <= c[-1]:
                    tmp += 1
            answer.append(tmp)
        
        return answer