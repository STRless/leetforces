# Category: BFS
# Time Complexity: O(max(x, y))
# Space Complexity: O(max(x, y)) worst case decrements or increments from x->y
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        visited = set()
        visited.add(x)
        q = deque()
        q.append((x, 0))
        while q:
            cur, steps = q.popleft()
            if cur == y:
                return steps
            if cur % 11 == 0 and cur//11 not in visited:
                visited.add(cur//11)
                q.append((cur//11, steps+1))
            if cur % 5 == 0 and cur//5 not in visited:
                visited.add(cur//5)
                q.append((cur//5, steps+1))
            if cur - 1 not in visited:
                visited.add(cur-1)
                q.append((cur-1, steps+1))
            if cur + 1 not in visited:
                visited.add(cur+1)
                q.append((cur+1, steps+1))
        return -1
