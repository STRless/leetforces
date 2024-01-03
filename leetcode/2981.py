# Topics: Bruteforce
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def maximumLength(self, s: str) -> int:
        temp = ""
        n = len(s)
        ans = -1
        for i in range(n):
            if temp == "" or temp[-1] != s[i]:
                temp = s[i]
            else:
                temp += s[i]
            ss = []
            cnt = 0
            for j in range(n):
                if s[j] != temp[0]:
                    ss = []
                else:
                    ss.append(temp[0])
                    if "".join(ss) == temp:
                        cnt += 1
                        ss.pop()
            if cnt >= 3:
                ans = max(ans, len(temp))
        return ans