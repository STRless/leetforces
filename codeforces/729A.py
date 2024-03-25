import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    i = 0
    cur = ""
    while i < n:
        if i + 2 < n and s[i] == 'o' and s[i+1] == 'g' and s[i+2] == 'o':
            j = i + 3
            while j < n:
                if j + 1 < n and s[j] == 'g' and s[j+1] == 'o':
                    j += 2
                else:
                    break
            i = j
            cur += "***"
        else:
            cur += s[i]
            i += 1
    sys.stdout.write(f"{cur}")



if __name__ == "__main__":
    main()