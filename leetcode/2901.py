class Solution:
    def getHammingDistance(self, word1, word2):
        if len(word1) != len(word2):
            return -1
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        return cnt
            
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if groups[i] != groups[j] and self.getHammingDistance(words[i], words[j]) == 1:
                    adj[words[i]].append(words[j])
        
        @cache
        def dfs(word):
            if word not in adj:
                return [word]
            
            longest = 0
            res = []
            for w in adj[word]:
                temp = dfs(w)
                if len(temp) > longest:
                    longest = len(temp)
                    res = temp
            return [word]+res

        long_len = 0
        ans = []
        for word in words:
            temp = dfs(word)
            if len(temp) > long_len:
                long_len = len(temp)
                ans = temp
        return ans