password = "notgoodatmath"
password_input = input("Enter the password: ")

def main():

    while True:
        question = input("[M]ultiply, [A]dd?, [S]ubtract, [D]ivide, or [Q]uit: ")
        x = int(input("Enter number 1: "))
        y = int(input("Enter number 2: "))
        question = question.upper()
        if question == "M":
            multiply(x,y)

        elif question == "S":
            subtract(x,y)
        elif question == "A":
            add(x,y)
        elif question == "D":
            Divide(x,y)
        elif question.lower() == "Q":
            break
        else:
            print("Enter a valid number!")





def multiply(x,y):
    multiply_input = x * y
    print(multiply_input)

def subtract(x,y):
    subtract_input = x - y
    print(subtract_input)

def add(x,y):
    add_input = x + y
    print(add_input)
def Divide(x,y):
    divide_input = x/y
    print(divide_input)


if password_input == "notgoodatmath":
    main()
else:
    print("Access denied.")



