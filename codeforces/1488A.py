import sys
     
     
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, y = map(int, sys.stdin.readline().split())
        ans = 0
        k = 0
        while k < y:
            temp = (y-k) // x
            digits = len(str(temp)) - 1
            val = (x*(10**digits))
            if y-k >= val:
                k += val
                ans += 1
            else:
                ans += (y - k)
                k = y
        sys.stdout.write(f"{ans}\n")
    
    
if __name__ == "__main__":
    main()