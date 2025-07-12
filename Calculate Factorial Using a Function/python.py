def factorial(num):
    if(num< 1):
        return 1
    else:
        return num * (factorial(num-1))

number = int(input("Enter a number :"))
ans = factorial(number)

print(f"Factorial of {number} is :" ,ans)