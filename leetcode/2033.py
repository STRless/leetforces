class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        choice = [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i]))]
        choice.sort()
        for i in range(1,len(choice)):
            if choice[i] % x != choice[i-1] % x:
                return -1
        
        mid = len(choice)//2
        ans = 0
        for c in choice:
            rem = abs(choice[mid]-c)
            ans += rem // x
        return ans