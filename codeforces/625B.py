import sys


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    ans = 0
    i = 0
    while i < len(s1) - len(s2)+1:
        j = 0
        flag = True
        while j < len(s2):
            if s1[i+j] != s2[j]:
                flag = False
                break
            j += 1
        if flag:
            ans += 1
            i += j
        else:
            i += 1
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()