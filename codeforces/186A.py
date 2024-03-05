import sys
from collections import Counter


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    if cnt1 != cnt2 or len(s1) != len(s2):
        sys.stdout.write("NO")
        return
    
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    if cnt != 2:
        sys.stdout.write("NO")
    else:
        sys.stdout.write("YES")
    

if __name__ == "__main__":
    main()