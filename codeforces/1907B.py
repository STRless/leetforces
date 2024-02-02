import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        res = []
        lower = 0
        upper = 0
        for i in reversed(range(len(s))):
            if s[i] == 'b':
                lower += 1
            elif s[i] == 'B':
                upper += 1
            else:
                if s[i].isupper():
                    if upper:
                        upper -= 1
                    else:
                        res.append(s[i])
                else:
                    if lower:
                        lower -= 1
                    else:
                        res.append(s[i])
        res.reverse()
        ans = "".join(res)
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()