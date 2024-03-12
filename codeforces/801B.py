import sys


def main():
    x = sys.stdin.readline().strip()
    y = sys.stdin.readline().strip()
    ans = ""
    flag = False
    for i in range(len(x)):
        if x[i] == y[i]:
            ans += x[i]
        elif x[i] > y[i]:
            ans += y[i]
        else:
            flag = True
            break
    if flag:
        print(-1)
    else:
        print(ans)



if __name__ == "__main__":
    main()