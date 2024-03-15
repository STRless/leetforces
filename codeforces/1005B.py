import sys


def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    
    i = len(s) - 1
    j = len(t) - 1
    while i >= 0 and j >= 0:
        if s[i] != t[j]:
            break
        i -= 1
        j -= 1
    sys.stdout.write(f"{i+j+2}")


if __name__ == "__main__":
    main()