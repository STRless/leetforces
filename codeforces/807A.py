import sys


def main():
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    changed = False
    for a, b in arr:
        if a != b:
            changed = True
    
    arr2 = arr.copy()
    arr2.sort(reverse=True)
    if changed:
        sys.stdout.write("rated\n")
    elif arr2 != arr:
        sys.stdout.write("unrated\n")
    else:
        sys.stdout.write("maybe\n")



if __name__ == "__main__":
    main()