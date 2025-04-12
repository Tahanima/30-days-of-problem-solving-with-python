def main():
    while True:
        x0 = input()

        if x0 == "END":
            break

        if x0 == "1":
            print(1)
        
        else:
            x0 = len(x0)
            xn = 0
            i = 2
            
            while True:
                xn = len(str(x0))
                
                if xn == x0:
                    print(i)
                    break
                
                i += 1
                x0, xn = xn, x0

if __name__ == "__main__":
    main()