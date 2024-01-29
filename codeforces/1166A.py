import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())

    class1 = defaultdict(int)
    class2 = defaultdict(int)
    ans = 0
    for _ in range(n):
        s = sys.stdin.readline().strip()
        if class1[s[0]] < class2[s[0]]:
            ans += class1[s[0]]
            class1[s[0]] += 1
        elif class2[s[0]] < class1[s[0]]:
            ans += class2[s[0]]
            class2[s[0]] += 1
        else:
            ans += class1[s[0]]
            class1[s[0]] += 1
    
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()