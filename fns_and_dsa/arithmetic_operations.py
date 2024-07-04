def perform_operation(x,y,z):
    r = 0
    match z : 
        case "add" : r= x+y
        case "subtract" : r= x-y
        case "multiply" : r= x*y
        case "divide" : r= x/y
    return r

print( perform_operation(4,5,"add"))

