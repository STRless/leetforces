import sys


def main():
    m = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    x, y = map(int, sys.stdin.readline().split())

    for i in range(1, m):
        first = sum(students[:i])
        second = sum(students[i:])
        if first >= x and first <= y and second >= x and second <= y:
            print(i+1)
            return
    print(0)



if __name__ == "__main__":
    main()