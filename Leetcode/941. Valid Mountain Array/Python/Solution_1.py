class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) >= 3:
            
            previous = arr[0]
            
            increasing = True
            decreasing = False
            
            for i in range(1,len(arr)):
                
                if increasing == True:
                    if previous < arr[i]:
                        previous = arr[i]
                    elif previous == arr[i]:
                        return False
                    elif previous > arr[i] and previous != arr[0]:
                        increasing = False
                        decreasing = True
                        previous = arr[i]
                
                elif decreasing == True:
                    if previous > arr[i]:
                        previous = arr[i]
                    elif previous == arr[i]:
                        return False
                    elif previous < arr[i]:
                        return False
            
            return True if decreasing == True else False
        return False