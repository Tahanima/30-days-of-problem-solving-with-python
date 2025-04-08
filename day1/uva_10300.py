def main():
    test_cases = int(input())

    for _ in range(test_cases):
        number_of_farmers = int(input())
        answer = 0

        for _ in range(number_of_farmers):
            data = list(map(int, input().split()))
            answer += (data[0] * data[2])
        
        print(answer)

if __name__ == "__main__":
    main()