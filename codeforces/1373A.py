import sys
import heapq

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().split())
        p1 = float(a)
        p2 = c/b
        if p1 < p2:
            sys.stdout.write(f"{a} {-1}\n")
        elif p1 > p2:
            sys.stdout.write(f"{cnt} {-1}\n")
        else:
            cnt = 1
            while True:
                if b % cnt:
                    break
                cnt += 1
            sys.stdout.write(f"{cnt} {-1}\n")



if __name__ == "__main__":
    main()