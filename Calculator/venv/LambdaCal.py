Add = lambda x,y : x+y
Diff = lambda x,y : x-y
Div = lambda x,y : x/y
Mult = lambda x,y : x*y

def Menu() :
    """this function prints the menu layout """
    print("\nWELCOME TO CALCULATOR\n")
    print("Press 1 to Add")
    print("Press 2 to Subtract")
    print("Press 3 to Multiply")
    print("Press 4 to Divide")
    print("print 5 to exit")

choice=1
while choice != 5:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    Menu()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print(Add(num1, num2))
    elif choice == 2:
        print(Diff(num1, num2))
    elif choice == 3:
        print(Mult(num2, num1))
    elif choice == 4:
        print(Div(num1, num2))
    elif choice == 5:
        print("THANK YOU!!!")
    else:
        print("INVALID INPUT ")
