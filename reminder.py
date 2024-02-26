
import time 
def set_reminder():
    reminder = input("What shall I remind you about? ")
    minutes = float(input("In how many minutes? "))
    return reminder, minutes

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

def main():
    reminder, minutes = set_reminder()
    print("Reminder set for:", reminder)
    time.sleep(minutes * 60)
    print("Reminder:", reminder)
    notify("Reminder", reminder)

if _name_ == "_main_":
    main()
