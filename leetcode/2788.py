class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            temp = word.split(separator)
            for t in temp:
                if t != "":
                    ans.append(t)
        return ans
            