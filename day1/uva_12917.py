import sys

def main():
    for line in sys.stdin:
        p, h, o = map(int, line.strip().split())
        print("Hunters win!" if ((o -p) < h) else "Props win!")

if __name__ == "__main__":
    main()