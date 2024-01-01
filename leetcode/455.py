# Topic: Array, Sorting
# Time Complexity: O(nm) where n is g.length and m is s.length
# Space Complexity: O(n+m) due to sort function
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        ans = 0
        for child in g:
            while j < len(s):
                if s[j] >= child:
                    ans += 1
                    j += 1
                    break
                j += 1
        return ans