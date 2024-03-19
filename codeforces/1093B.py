import sys
from collections import Counter

def is_palindrome(s):
    n = len(s)
    lo = 0
    hi = n-1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True



def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        if is_palindrome(s) and len(Counter(s)) == 1:
            sys.stdout.write("-1\n")
        else:
            if (is_palindrome(s)):
                temp = list(s)
                for i in range(1, len(s)):
                    if temp[i] != temp[0]:
                        temp[i], temp[0] = temp[0], temp[i]
                        break
                res = "".join(temp)
                sys.stdout.write(f"{res}\n")
            else:
                sys.stdout.write(f"{s}\n")


if __name__ == "__main__":
    main()