import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def division(n1, n2):
    if n2==0:

        return "Error: divisible by 0  "
    return n1/n2

operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1=float(input("enter the  first number:  "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        op=input("pick any operation :  ")
        if op  not in operations:
            print("enter the valid operation")
            continue
        num2=float(input("enter the second number:  "))
        solution=operations[op](num1,num2)
        print(f"{num1} {op} {num2} = {solution}")

        choice=input(f"enter 'y' to continue with {solution} or 'n' to start without previous output ")

        if choice=="y":
            num1=solution

        else :
            should_accumulate=False
            print("\n"* 20)
            calculator()
calculator()