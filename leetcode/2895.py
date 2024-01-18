class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        ans = float('-inf')
        i = 0
        for p in processorTime:
            j = 0
            while j < 4:
                ans = max(ans, p + tasks[i])
                i += 1
                j += 1
        return ans
            