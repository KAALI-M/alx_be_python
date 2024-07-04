def perform_operation(num1, num2, operation):
    res = 0
    match operation : 
        case "add": res = num1+num2
        case "subtract": res = num1-num2
        case "multiply": res = num1*num2
        case "divide": res = num1/num2
    
    return res

print(perform_operation(5,6,"divide"))
