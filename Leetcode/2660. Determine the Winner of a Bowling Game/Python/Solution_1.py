class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        double_1 = 0
        double_2 = 0

        point_1 = 0
        point_2 = 0

        for n1,n2 in zip(player1,player2):
            if double_1 > 0 :
                point_1 += n1 * 2
                double_1 -= 1
                if n1 == 10:
                    double_1 = 2                
            else:
                point_1 += n1
                if n1 == 10:
                    double_1 = 2
            
            if double_2 > 0 :
                point_2 += n2 * 2
                double_2 -= 1
                if n2 == 10:
                    double_2 = 2
            else:
                point_2 += n2
                if n2 == 10:
                    double_2 = 2
        
        if point_2 == point_1:
            return 0
        if point_1 > point_2: 
            return 1 
        if point_2 > point_1:
            return 2 