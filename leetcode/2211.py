class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        n = len(directions)
        r = l = 0
        directions = list(directions)
        for i in range(n):
            if directions[i] == 'R':
                r += 1
            elif directions[i] == 'L':
                ans += r
                if r > 0:
                    ans += 1
                    directions[i] = 'S'
                r = 0
            else:
                ans += r
                r = 0
        for i in range(n-1, -1, -1):
            if directions[i] == 'L':
                l += 1
            elif directions[i] == 'S':
                ans += l
                l = 0
        return ans