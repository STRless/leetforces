import sys


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        s = sys.stdin.readline().strip()
        flag = False
        for i in range(1, len(s)):
            if s[i] == '?':
                continue
            if s[i] == s[i-1]:
                flag = True
                break
        if flag:
            sys.stdout.write("-1\n")
        else:
            check = list(s)
            for i in range(len(s)):
                temp = set()
                if check[i] == '?':
                    if i == 0:
                        pass
                    else:
                        temp.add(check[i-1])
                    if i+1 < len(s) and check[i+1] != '?':
                        temp.add(check[i+1])
                    for ch in ['a', 'b', 'c']:
                        if ch not in temp:
                            check[i] = ch
                            break
            res = "".join(check)
            sys.stdout.write(f"{res}\n")


if __name__ == "__main__":
    main()
