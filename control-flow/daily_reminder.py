# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the priority using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unrecognized priority level"

# Check if the task is time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["high", "medium"]:
        message += ". Try to complete it soon."
    else:
        message += ". Consider completing it when you have free time."

# Print the final customized reminder
print("\n" + message)
