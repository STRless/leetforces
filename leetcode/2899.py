class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        cnt = 0
        ans = []
        nums_reverse = deque()
        for i, word in enumerate(words):
            if word == "prev":
                cnt += 1
                if cnt > len(nums_reverse):
                    ans.append(-1)
                else:
                    ans.append(int(nums_reverse[cnt-1]))
            else:
                cnt = 0
                nums_reverse.appendleft(word)
        return ans
                
                