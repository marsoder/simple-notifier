from datetime import datetime, timedelta
import gi
import argparse
from gi.repository import Gio

class Trigger:
    NOW = datetime.now()

    def __init__(self, seconds=0, minutes=0, hours=0):

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def __repr__(self):
        return f"<Notification(seconds = {self.seconds}, hours = {self.hours}, message = {self.message}), {hex(id(self))}>"

    def display_when(self):
        return self.NOW + timedelta(hours=self.hours, minutes=self.minutes, seconds=self.seconds)


    def total_seconds(self):
        return (self.hours * 60**2) + (self.minutes*60) + (self.seconds)

    def time_elapsed(self):
        return str(timedelta(seconds=self.total_seconds()))

class Notification:    
    DEFAULT_MESSAGE = "Time is up"
    def __init__(self, trigger_timestamp=None, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        self.trigger_timestamp = trigger_timestamp
    def display_notification(self):
        Application = Gio.Application.new(
            "my.program", Gio.ApplicationFlags.FLAGS_NONE)
        Application.register()
        Notification = Gio.Notification.new("Notification")
        Notification.set_body(f"{self.message}")
        Icon = Gio.ThemedIcon.new("dialog-information")
        Notification.set_icon(Icon)
        Application.send_notification(None, Notification)
