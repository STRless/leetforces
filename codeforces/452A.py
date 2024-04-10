import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    pokemon = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]

    for p in pokemon:
        if n == len(p):
            flag = True
            for i in range(n):
                if s[i] != '.' and s[i] != p[i]:
                    flag = False
            if flag:
                print(p)



if __name__ == "__main__":
    main()