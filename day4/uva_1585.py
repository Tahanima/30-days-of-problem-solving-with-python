import sys

def main():
    lines = sys.stdin.read().splitlines()
    write = sys.stdout.write
    idx = 0

    n = int(lines[idx].strip())
    idx += 1

    for _ in range(n):
        result = lines[idx].strip()
        idx += 1
        
        sum = 0
        zeros = 0

        for i in range(len(result)):
            if result[i] == 'O':
                zeros += 1
                sum += zeros
            else:
                zeros = 0
        
        write(f"{sum}\n")


if __name__ == "__main__":
    main()