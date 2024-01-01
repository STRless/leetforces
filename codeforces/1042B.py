import sys
from functools import cache

sys.setrecursionlimit(10**4)

# Topics: DP


def main():
    n = int(sys.stdin.readline())

    choices = []
    for _ in range(n):
        c, s = map(str, sys.stdin.readline().split())
        c = int(c)
        choices.append((c, s))
    
    @cache
    def dfs(i=0, a=False, b=False, c=False):
        if a and b and c:
            return 0
        elif i >= n:
            return float('inf')

        temp = float('inf')
        # dont make the purchase
        temp = min(temp, dfs(i+1, a, b, c))

        #make the purchase
        if 'A' in choices[i][1]:
            a = True
        if 'B' in choices[i][1]:
            b = True
        if 'C' in choices[i][1]:
            c = True
        temp = min(temp, dfs(i+1, a, b, c) + choices[i][0])
        return temp
    
    res = dfs()
    if res == float('inf'):
        res = -1
    sys.stdout.write("{}\n".format(res))


if __name__ == "__main__":
    main()