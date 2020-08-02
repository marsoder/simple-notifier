from Notifier.argparser import create_parser, parse_arguments
from Notifier.notifier import Notification
def arguments():
    parser = create_parser()
    args = parse_arguments(parser)
    return args.seconds, args.hours

if __name__ == "__main__":
   seconds, hours = arguments()
   notification = Notification(seconds,hours)
   print(notification)
