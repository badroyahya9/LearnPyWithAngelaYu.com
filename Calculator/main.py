def add(n1, n2) :
    return n1 + n2

def subtract(n1, n2) :
    return n1 - n2

def multiply(n1, n2) :
    return n1 * n2

def divide(n1, n2) :
    return n1 / n2

dictionary_of_operations = { 
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

import art
print(art.logo)

result = 0
calculating = True
while calculating :

    if result == 0:
        first_num = float(input("Type the first number: "))
    
    print("""
+
-
*
/
    """)
    opiration = input("pick up an operation : ")
    next_num = float(input("Type the next number: "))

    result = dictionary_of_operations[opiration](n1= first_num, n2= next_num)
    print(f"{first_num} {opiration} {next_num} = {result}")

    y_or_n = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if y_or_n == "n" :
        print("\n" * 50)
        print(art.logo)
        result = 0
    else :
        first_num = result
