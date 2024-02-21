import sys


def main():
    n = int(sys.stdin.readline())
    robo = list(map(int, sys.stdin.readline().split()))
    bionic = list(map(int, sys.stdin.readline().split()))
    if robo == bionic:
        sys.stdout.write("-1")
        return
    
    rc = bc = 0
    for i in range(len(robo)):
        if robo[i] == 1 and bionic[i] == 0:
            rc += 1
        elif robo[i] == 0 and bionic[i] == 1:
            bc += 1
    
    if rc > bc:
        sys.stdout.write("1")
    elif rc == bc:
        sys.stdout.write("2")
    elif rc == 0:
        sys.stdout.write("-1")
    else:
        res = (bc//rc) + 1
        sys.stdout.write(f"{res}")


if __name__ == "__main__":
    main()