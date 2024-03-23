import sys


def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    sh = int(s[:2])
    th = int(t[:2])
    sm = int(s[3:])
    tm = int(t[3:])
    hm = sm - tm
    hr = sh - th
    if hm < 0:
        hr -= 1
        hm = 60 - abs(hm)

    if hr < 0:
        hr = 24 - abs(hr)
    
    if hr < 10:
        hr = str(hr)
        sys.stdout.write(f"0{hr}:")
    else:
        hr = str(hr)
        sys.stdout.write(f"{hr}:")
    if hm < 10:
        hm = str(hm)
        sys.stdout.write(f"0{hm}")
    else:
        hm = str(hm)
        sys.stdout.write(f"{hm}")
    

    



if __name__ == "__main__":
    main()