def main():
    n = int(input())
    positive = ["1", "4", "78"]

    for _ in range(n):
        m = input()

        if m in positive:
            print("+")
        elif m[-2:] == "35":   
            print("-")
        elif m[0] == "9" and m[-1] == "4":
            print("*")
        else:
            print("?")

if __name__ == "__main__":
    main()