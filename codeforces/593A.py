import sys


def main():
    n = int(sys.stdin.readline())
    words = []
    for _ in range(n):
        s = sys.stdin.readline().strip()
        if len(set(list(s))) > 2:
            continue
        words.append(s)
    
    ans = 0
    for word1 in words:
        w1 = set(word1)
        if len(w1) == 2:
            cnt = 0
            for word2 in words:
                w2 = set(word2)
                if w1.union(w2) == w1:
                    cnt += len(word2)
            ans = max(ans, cnt)
        else:
            for word2 in words:
                check = w1.union(set(word2))
                if len(check) <= 2:
                    cnt = 0
                    for word3 in words:
                        w3 = set(word3)
                        if check.union(w3) == check:
                            cnt += len(word3)
                    ans = max(ans, cnt)
    sys.stdout.write(f"{ans}\n")




if __name__ == "__main__":
    main()