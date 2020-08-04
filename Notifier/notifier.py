from datetime import datetime, timedelta
import gi
from gi.repository import Gio

class TriggerTime:
    def __init__(self, seconds=0, minutes=0, hours=0):

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    @property
    def seconds(self): return self._seconds

    @property
    def minutes(self): return self._minutes

    @property
    def hours(self): return self._hours

    @seconds.setter
    def seconds(self, value):
        if value > 59:
            raise ValueError("seconds must be 0-59")
        self._seconds = value

    @minutes.setter
    def minutes(self, value):
        if value > 59:
            raise ValueError("minutes must be 0-59")
        self._minutes = value

    @hours.setter
    def hours(self, value):
        if value > 23:
            raise ValueError("hours must be 0-23")
        self._hours = value
        
    @property
    def total_seconds(self):
        return (self.hours * 60**2) + (self.minutes*60) + (self.seconds)

    @property
    def time_elapsed(self):
        return str(timedelta(seconds=self.total_seconds))

class Notification:    
    def __init__(self, message, time_elapsed=None):
        self.message = message
        self.time_elapsed = time_elapsed
        if time_elapsed:
            self.message += "\n" + f"Time elapsed: {time_elapsed}"
            
    def display_notification(self):
        Application = Gio.Application.new(
            "my.program", Gio.ApplicationFlags.FLAGS_NONE)
        Application.register()
        Notification = Gio.Notification.new("Notification")
        Notification.set_body(f"{self.message}")
        Icon = Gio.ThemedIcon.new("dialog-information")
        Notification.set_icon(Icon)
        Application.send_notification(None, Notification)
