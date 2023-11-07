num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

def compute(num1, num2):
    # Actual Value Computation
    sum = num1 + num2
    diff = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    print("")

    # Sum
    print("Sum:", sum)
    if sum > 0:
        print("The sum is positive.\n")
    else:
        print("The sum is negative.\n")

    # Difference
    print("Difference:", diff)
    if diff > 0:
        print("The difference is positive.\n")
    else:
        print("The difference is negative.\n") 
    
    # Product
    print("Product:", mult)
    if mult > 0:
        print("The product is positive.\n")
    else:
        print("The product is negative.\n")

    # Quotient
    print("Quotient (Rounded to 2 places):", f'{div:.2f}')
    if div > 0:
        print("The quotient is positive.\n")
    else:
        print("The quotient is negative.\n") 

    return compute

compute(num1, num2)

