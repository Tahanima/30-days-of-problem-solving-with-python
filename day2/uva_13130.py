def main():
    n = int(input())

    for _ in range(n):
        nums = list(map(int, input().split()))
        is_escala = True
        
        for i in range(1, 5):
            if nums[i] - nums[i - 1] != 1:
                is_escala = False
                break
        
        print("Y" if is_escala else "N")

if __name__ == "__main__":
    main()