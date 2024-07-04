from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now()
    return current_date 

def calculate_future_date(n,datenow=datetime.now()):
    future_date = datenow + timedelta(days=n)
    return future_date

print(f"Current date and time: {display_current_datetime().strftime("%Y-%m-%d %H:%M:%S")}")
number_of_days = int(input("enter a number of daysEnter the number of days to add to the current date: "))
future_date = calculate_future_date(number_of_days,display_current_datetime())
print(f"Future date: {future_date.strftime("%d-%m-%Y")}")






