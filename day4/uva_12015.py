import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    write = sys.stdout.write

    test_cases = int(input().strip())

    for i in range(test_cases):
        webpage_relevance = defaultdict(list)
        max_relevance = 0

        for _ in range(10):
            webpage, relevance = input().strip().split()
            relevance = int(relevance)
            max_relevance = max(max_relevance, relevance)
            webpage_relevance[relevance].append(webpage)

        write(f"Case #{i + 1}:\n")
        for page in webpage_relevance[max_relevance]:
            write(page + "\n")

if __name__ == "__main__":
    main()