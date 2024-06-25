x = int(input("Enter the size of the pattern: "))
i=j=x
while j > 0 :
    i=x 
    while i > 0 :
        if i > 1 :print("*", end="")
        else : print("*")
        i-=1
    j-=1


