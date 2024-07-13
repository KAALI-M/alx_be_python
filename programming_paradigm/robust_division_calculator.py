def safe_divide(numerator, denominator):
  try:
    if isinstance(numerator,(int,float))==False or isinstance(denominator,(int,float))==False :
      raise ValueError("errorNonNumeric")
    res = float(numerator)/float(denominator)
    return (f"The result of the division is {res:.1f}")

  except ValueError as e:
    if str(e)=="errorNonNumeric" : 
      return ("Error: Please enter numeric values only.")
    else:
      return ("erro:r: ",e)
  except ZeroDivisionError:
    return("Error: Cannot divide by zero.")  

print(safe_divide(10.1,10.1))
