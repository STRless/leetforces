import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        nums = list(map(int, sys.stdin.readline().split()))
        min_num = min(nums)
        for i, num in enumerate(nums):
            if num == min_num:
                nums[i] += 1
                break
        ans = nums[0]
        for num in nums[1:]:
            ans *= num
        sys.stdout.write("{}\n".format(ans))


if __name__ == "__main__":
    main()