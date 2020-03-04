def Fibonacci_of(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        return Fibonacci_of(num - 1) + Fibonacci_of(num - 2)

def main():
    for i in range(1,201):
        print("Fibonacci_of(" + str(i) + ") = " + str(Fibonacci_of(i)))

if __name__ == '__main__':
    main()