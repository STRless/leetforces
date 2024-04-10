import sys
from itertools import permutations

def main():
    t = int(sys.stdin.readline())
    perms = list(permutations([0, 1, 2, 3, 4, 5, 6]))
    for _ in range(t):
        arr = list(map(int, sys.stdin.readline().split()))

        combo = [(0, 1, 0), (1, 0, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
        ans = 0
        for perm in perms:
            temp = arr.copy()
            t = 0
            for p in perm:
                if temp[0] >= combo[p][0] and temp[1] >= combo[p][1] and temp[2] >= combo[p][2]:
                    t += 1
                    temp[0] -= combo[p][0]
                    temp[1] -= combo[p][1]
                    temp[2] -= combo[p][2]
            ans = max(ans, t)
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()
