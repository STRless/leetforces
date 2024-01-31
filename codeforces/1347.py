import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        st = []

        for ch in s:
            if ch == '(':
                st.append(ch)
            else:
                if st:
                    st.pop()
        sys.stdout.write(f"{len(st)}\n")


if __name__ == "__main__":
    main()