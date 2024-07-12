def safe_divide(numerator, denominator):
  try:

    res = float(numerator)/float(denominator)
    
    if isinstance(numerator,(int,float))==False or tisinstance(denominator,(int,float))==False :
      raise ValueError("errorNonNumeric")
    print(f"The result of the division is {res:.1f}")
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  except ValueError as e:
    if str(e)=="errorNonNumeric" : 
      print("Error: Please enter numeric values only.")
    else:
      print("erro:r: ",e)
