def perform_operation(num1, num2, operation):
    r = 0
    if operation == "add" : r= num1+num2
    elif operation ==  "subtract" : r= num1-num2
    elif operation ==  "multiply" : r= num1*num2
    elif operation ==  "divide" :
        if num2 == 0 : print("division by 0")
        else  : r= num1/num2
    return r

print( perform_operation(4,0,"divide"))

