class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        counter = 0

        while counter < len(arr)-1:
            if arr[counter] == 0:
                tmp = arr[counter+1]
                arr[counter+1] = 0
                for i in range(counter+2,len(arr)):
                    tmp2 = arr[i]
                    arr[i] = tmp
                    tmp = tmp2
                counter += 1
            counter+=1
        
        # poor solution