import sys

def main():
    test_case = 1
    
    for line in sys.stdin:
        r, n = map(int, line.strip().split())

        if (r + n) == 0:
            break

        n = (r // n) + (1 if r % n != 0 else 0) - 1

        print(f"Case {test_case}: {n if n <= 26 else 'impossible'}")
        
        test_case += 1


if __name__ == "__main__":
    main()