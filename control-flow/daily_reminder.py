task= input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
Time_bound = input("Is it time-bound? (yes/no): ")

match priority : 
    case "high":
        msg= task +" is a high priority task"
    case "medium": 
        msg= task +" is a medium priority task"
    case "low": 
        msg= task +" is a low priority task"
    case _ :
        msg= "the priority is anknown"

if Time_bound == "yes" :
    Reminder = "Reminder:" + msg + " tasthat requires immediate attention today!"
else :
   reminder = "Note: '" +msg+ ". Consider completing it when you have free time."
    print ( "Reminder: ", reminder)


