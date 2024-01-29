import sys

def main():
    n = int(sys.stdin.readline())
    if n < 10:
        sys.stdout.write("1")
    else:
        remain = str(n)[1:]
        temp = "1"
        temp += ('0' * len(remain))
        sys.stdout.write(f"{int(temp) - int(remain)}")

if __name__ == "__main__":
    main()