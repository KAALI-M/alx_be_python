def safe_divide(numerator, denominator):
  try:
    if type(numerator) or type(denominator) :
      raise ValueError("errorNonNumeric")
    res = float(numerator)/float(denominator)
    print(f"The result of the division is {res:.1f}")
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  except ValueError as e:
    if str(e)=="errorNonNumeric" : 
      print("Error: Please enter numeric values only.")
    else
      print("erro:r: ",e)
