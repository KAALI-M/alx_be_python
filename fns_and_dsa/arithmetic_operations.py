def perform_operation(num1,num2,operation):
    r = 0
    match z : 
        case "add" : r= num1+num2
        case "subtract" : r= num1-num2
        case "multiply" : r= num1*num2
        case "divide" : r= num1/num2
    return r

print( perform_operation(4,5,"add"))

