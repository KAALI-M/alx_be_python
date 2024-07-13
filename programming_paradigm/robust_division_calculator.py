<<<<<<< HEAD
def safe_divide(numerator, denominator):
  try:
    nom = float(numerator)
    denom = float(denominator)
    result = nom/denom
    return f"he result of the division is {result:.1f}"
  except ZeroDivisionError : 
    return "'Error: Cannot divide by zero.'"
  except ValueError: 
    return "Error: Please enter numeric values only."

print (safe_divide(10.25,"ten"))
=======

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result:.1f}"
    
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
    except ValueError:
        return 'Error: Please enter numeric values only.'
>>>>>>> 5f1d782e205b06316326d1e72554ffb3ca2ed48e
