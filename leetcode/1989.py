class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        n = len(team)
        indices = deque()
        for i, num in enumerate(team):
            if num == 0:
                indices.append(i)
        
        ans = 0
        for i, num in enumerate(team):
            if num == 1:
                low = i - dist
                high = i + dist
                while indices:
                    if indices[0] < low:
                        indices.popleft()
                    else:
                        if indices[0] <= high:
                            ans += 1
                            indices.popleft()
                        break
        return ans
                    