num1 = float(input("Enter the first number: "))
num2 = float (input ("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /): ")
match operation :
    case "+" : print("The result is ",num1+num2)
    case "-" : print("The result is ",num1-num2)
    case "*" : print("The result is ",num1*num2)
    case "/" : 
        if (num2 != 0) : print("The result is ", num1/num2)
        else : print("Cannot divide by zero.")
    case _: print("the operation is not rcognized")


    
