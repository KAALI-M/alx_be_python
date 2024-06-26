task= input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
Time_bound = input("Is it time-bound? (yes/no): ")

match priority : 
    case "high"|"medium"|"low": 
        msg= task +" is a high priority task"
    case _ :
        msg= "the priority is anknown"

if Time_bound == "yes" :
    msg = "Reminder : '" + msg + " tasthat requires immediate attention today!"
else :
    msg = "Note : '" +msg+ ". Consider completing it when you have free time."

print(msg)
