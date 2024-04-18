import sys


def main():
    t = sys.stdin.readline().strip()
    i = 0
    a_cnt = 0
    while i < len(t) and t[i] == 'a':
        a_cnt += 1
        i += 1
    
    b_cnt = 0
    while i < len(t) and t[i] == 'b':
        b_cnt += 1
        i += 1
    c_cnt = 0
    while i < len(t) and t[i] == 'c':
        c_cnt += 1
        i += 1
    if i == len(t) and (c_cnt == a_cnt or c_cnt == b_cnt) and a_cnt and b_cnt and c_cnt:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()