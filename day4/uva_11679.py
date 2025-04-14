import sys

def main():
    lines = sys.stdin.read().splitlines()
    write = sys.stdout.write
    idx = 0

    while idx < len(lines):
        b, n = map(int, lines[idx].strip().split())
        idx += 1

        if b == 0 and n == 0:
            break

        banks = list(map(int, lines[idx].strip().split()))
        idx += 1

        for _ in range(n):
            d, c, v = map(int, lines[idx].strip().split())
            banks[d - 1] -= v
            banks[c - 1] += v
            idx += 1

        has_negative = any(val < 0 for val in banks)
        write("N\n" if has_negative else "S\n")

if __name__ == "__main__":
    main()
