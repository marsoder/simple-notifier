from Notifier.argparser import create_parser, parse_arguments, get_arguments
from Notifier.notifier import Notification, TriggerTime
import time

def main():
    seconds, minutes, hours, message  = get_arguments()
    trigger = TriggerTime(seconds, minutes, hours)
    notification = Notification(message, time_elapsed=trigger.time_elapsed)
    time.sleep(trigger.total_seconds)
    notification.display_notification()
if __name__ == "__main__":
    main()

    # 1. parse arguments
    # 2. create notificaion instance with message
    # 3. sleep during the desired duration
    # 4. display notification
    
    
