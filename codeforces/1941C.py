import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        cnt = s.count('pie')
        cnt += s.count('map')
        cnt -= s.count('mapie')
        sys.stdout.write(f'{cnt}\n')


if __name__ == '__main__':
    main()