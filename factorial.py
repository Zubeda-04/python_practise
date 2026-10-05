def fact(n):
    fact=1
    if n<0:
        print("Factorial should be a positive integer")
    elif n==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact*=i
        print(f"Factorial of {n} is {fact}")
fact(int(input("Enter a number: ")))
