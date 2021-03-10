def fib(n):
    # input check less than zero
    if n < 0:
        print("Incorrect input")
 
    # input check zero
    elif n == 0:
        return 0
 
    # input check 1 or 2
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fib(n-1) + fib(n-2)
 
n = int(input("Enter number of terms: "))
print(fib(n))