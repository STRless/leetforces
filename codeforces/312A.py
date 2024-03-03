import sys


def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        s = sys.stdin.readline().strip()
        if len(s) >= 5:
            if s[-5:] == "lala.":
                if s[:5] == "miao.":
                    sys.stdout.write("OMG>.< I don't know!\n")
                else:
                    sys.stdout.write("Freda's\n")
            else:
                if s[:5] == "miao.":
                    sys.stdout.write("Rainbow's\n")
                else:
                    sys.stdout.write("OMG>.< I don't know!\n")
        else:
            sys.stdout.write("OMG>.< I don't know!\n")


if __name__ == "__main__":
    main()