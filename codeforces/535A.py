import sys


def main():
    s = int(sys.stdin.readline())
    m = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7:"seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen"}
    if s in m:
        sys.stdout.write(f"{m[s]}")
    else:
        double = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
        if s % 10 == 0:
            sys.stdout.write(f"{double[s//10]}")
        else:
            sys.stdout.write(f"{double[s//10]}-{m[s%10]}")


if __name__ == "__main__":
    main()