class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = bob = 0
        i = 0
        while i < len(colors):
            j = i
            cnt = 0
            while j < len(colors) and colors[i] == colors[j]:
                cnt += 1
                j += 1
            if cnt >= 3:
                if colors[i] == 'A':
                    alice += cnt - 2
                else:
                    bob += cnt - 2
            i = j
        return alice > bob