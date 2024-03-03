import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    instr = []
    for i, a in enumerate(arr):
        instr.append((a, i+1))

    instr.sort()
    count = acc = 0
    indices = []
    for (a, i) in instr:
        if acc + a <= k:
            count += 1
            acc += a
            indices.append(i)
        else:
            break
    
    sys.stdout.write(f"{count}\n")
    for i in indices:
        sys.stdout.write(f"{i} ")
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()