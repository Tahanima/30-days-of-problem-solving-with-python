import sys

def main():
    data = sys.stdin.read().split()
    index = 0

    test_cases = int(data[index])
    index += 1

    for _ in range(test_cases):
        n = int(data[index])
        index += 1

        nums = list(map(int, data[index:index + n]))
        index += n

        min_n = [0] * n
        min_n[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            min_n[i] = min(nums[i], min_n[i + 1])

        ans = float('-inf')
        for i in range(n - 1):
            ans = max(ans, nums[i] - min_n[i + 1])

        print(ans)

if __name__ == "__main__":
    main()