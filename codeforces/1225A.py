import sys


def main():
    a, b = map(int, sys.stdin.readline().split())
    if a == 9 and b == 1:
        sys.stdout.write(f"99 100")
    elif abs(a-b) >= 2 or a > b:
        sys.stdout.write("-1")
    else:
        ans_a = str(a)
        ans_b = str(b)
        if a == b:
            ans_a += '1'
            ans_b += '2'
            sys.stdout.write(f"{ans_a} {ans_b}")
        else:
            ans_a += '9'
            ans_b += '0'
            sys.stdout.write(f"{ans_a} {ans_b}")

if __name__ == "__main__":
    main()