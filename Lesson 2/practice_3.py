process = input("please choice your operation: (-, +, /, *) ")
number_1 = float(input("enter first number: "))
number_2 = float(input("enter sec number: "))
if process == "*":
    result = number_1 * number_2
    print(result)

elif process == "/":
    result = number_1 / number_2
    print(result)

elif process == "+":
    result = number_1 + number_2
    print(result)

elif process == "-":
    result = number_1 - number_2
    print(result)