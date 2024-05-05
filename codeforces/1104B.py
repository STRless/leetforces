import sys


def main():
    s = sys.stdin.readline().strip()
    st = []
    turn = 0
    for ch in s:
        if st and ch == st[-1]:
            st.pop()
            turn += 1
        else:
            st.append(ch)
    if turn % 2 == 0:
        sys.stdout.write("No\n")
    else:
        sys.stdout.write("Yes\n")


if __name__ == "__main__":
    main()