import sys
from collections import defaultdict

def main():
    n, k = map(int, sys.stdin.readline().split())

    jobs = list(map(int, sys.stdin.readline().split()))
    times = list(map(int, sys.stdin.readline().split()))
    temp = []
    for i in range(n):
        temp.append((jobs[i], times[i]))
    
    check = defaultdict(int)
    temp.sort(key=lambda x: x[1])
    for i in range(len(temp)):
        check[temp[i][0]] += 1
    ans = 0
    filled = set()
    cnt = 0
    goal = k-len(check)
    for i in range(len(temp)):
        if cnt == goal:
            break
        job, time = temp[i][0], temp[i][1]
        if check[job] > 1:
            check[job] -= 1
            ans += time
            cnt += 1
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()