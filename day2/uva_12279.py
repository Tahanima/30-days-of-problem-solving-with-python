def main():
    test_case = 1

    while True:
        n = int(input())
        
        if n == 0:
            break

        nums = list(map(int, input().split()))

        print(f"Case {test_case}: {sum(-1 if i == 0 else 1 for i in nums)}")
        test_case += 1

if __name__ == "__main__":
    main()

