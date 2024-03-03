import sys


def main():
    s = sys.stdin.readline().strip()
    i = 0
    ans = "hello"
    for ch in s:
        if ch == ans[i]:
            i += 1
        if i == len(ans):
            break
    
    if i == len(ans):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()