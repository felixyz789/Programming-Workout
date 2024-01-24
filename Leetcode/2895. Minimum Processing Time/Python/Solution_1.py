class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sorted_task = sorted(tasks, reverse = True)
        sorted_time = sorted(processorTime)

        maximum = sorted_task[0] + sorted_time[0]

        for i in range(4,len(sorted_task),+4):
            max_time = sorted_task[i] + sorted_time[i // 4]
        
            maximum = max(maximum,max_time)
            
        return maximum
