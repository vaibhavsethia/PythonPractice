import re

print("WELCOME TO MY CALCULATOR ")
print("Note : type exit to quit\n")

previous = 0
run = True

def Calc() :
    global previous
    global run
    equation = ""
    if previous == 0 :
        equation = input("Enter the equation to evaluate : ")
    else :
        equation = input(str(previous))

    if equation =='quit' :
        print(" THNAK YOU!!!")
        run = False
    else :
        equation=re.sub('[A-Za-z]','',equation)
        if previous == 0 :
            previous = eval(equation)
        else :
            previous = eval(str(previous)+equation)


while run :
    Calc()
