from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now()
    return current_date 

def calculate_future_date(n,datenow=datetime.now()):
    future_date = datenow + timedelta(days=n)
    return future_date

print(f"Current date and time: {display_current_datetime().strftime("%x %X")}")
number_of_days = int(input("enter a number of daysEnter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(number_of_days,display_current_datetime()).strftime("%d-%m-%Y")}")






