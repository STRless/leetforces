# Topics: Brute Force
# Time Complexity: O(max(len(hFences), len(vFences)))
# Space Complexity: O(n^2) where n is length of hFences
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend((1, m))
        vFences.extend((1, n))
        check = set()
        ans = -1

        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                check.add(abs(hFences[i]-hFences[j]))

        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                temp = abs(vFences[i]-vFences[j])
                if temp in check:
                    ans = max(ans, temp**2)

        return -1 if ans == -1 else ans % (10**9+7)