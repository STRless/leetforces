class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < n:
            j = i
            word = ""
            while j < n and groups[j] == groups[i]:
                if len(words[j]) > len(word):
                    word = words[j]
                j += 1
            i = j
            ans.append(word)

        return ans