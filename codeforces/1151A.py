import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    ans = float('inf')
    def get_cost(orig, target):
        cost1 = abs(ord(orig)-ord(target))
        return min(cost1, 26-cost1)

    for i in range(n-3):
        temp = get_cost(s[i], 'A')
        temp += get_cost(s[i+1], 'C')
        temp += get_cost(s[i+2], 'T')
        temp += get_cost(s[i+3], 'G')
        ans = min(ans, temp)

    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()
