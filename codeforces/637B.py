import sys

def main():
    n = int(sys.stdin.readline())
    name_pos = {}
    pos_name = {}
    last = 0
    for _ in range(n):
        name = sys.stdin.readline().strip()
        name_pos[name] = last
        pos_name[last] = name
        last += 1
    
    check = set()
    for i in range(last, -1, -1):
        if i in pos_name and pos_name[i] not in check:
            check.add(pos_name[i])
            sys.stdout.write("{}\n".format(pos_name[i]))


if __name__ == "__main__":
    main()