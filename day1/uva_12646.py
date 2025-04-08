import sys

def main():
    for line in sys.stdin:
        a, b, c = map(int, line.strip().split())
        total = a + b + c

        if total in (0, 3):
            print("*")
        else:
            values = [a, b, c]
            index = values.index(1 if total == 1 else 0)
            print("ABC"[index])

if __name__ == "__main__":
    main()
