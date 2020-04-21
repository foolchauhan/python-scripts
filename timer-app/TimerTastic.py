import rumps

class TimerTasticApp(object):
    def __init__(self):

        self.config = {
            "app_name": "TimerTastic",
            "start": "Start Timer",
            "pause": "Pause Timer",
            "continue": "Continue Timer",
            "stop": "Stop Timer",
            "set": "Set Timer",
            "setMessage": "Set Message",
            "break_message": "Time is up! Take a break :)",
            "interval": 300
        }

        self.app = rumps.App(self.config["app_name"], "⏰" )
        self.timer = rumps.Timer(self.on_tick, 1)
        self.interval = self.config["interval"]
        self.break_message = self.config["break_message"]
        self.set_up_menu()
        self.start_pause_button = rumps.MenuItem(title=self.config["start"], callback=self.start_timer)
        self.stop_button = rumps.MenuItem(title=self.config["stop"], callback=None)
        self.set_button = rumps.MenuItem(title=self.config["set"], callback=self.set_timer)
        self.setMessage_button = rumps.MenuItem(title=self.config["setMessage"], callback=self.set_message)
        self.app.menu = [self.start_pause_button, self.stop_button, self.set_button, self.setMessage_button]

    def set_up_menu(self):
        self.timer.stop()
        self.timer.count = 0
        self.app.title = "⏰"        # ⏱

    def on_tick(self, sender):
        time_left = sender.end - sender.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            rumps.notification(title=self.config["app_name"], subtitle=self.break_message, message='')
            self.stop_timer(sender)
            self.stop_button.set_callback(None)
            self.set_button.set_callback(self.set_timer)
            self.setMessage_button.set_callback(self.set_message)
        else:
            self.stop_button.set_callback(self.stop_timer)
            self.set_button.set_callback(None)
            self.setMessage_button.set_callback(None)
            self.app.title = '{:2d}:{:02d}'.format(mins, secs)
        sender.count += 1

    def start_timer(self, sender):
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.config["start"]:
                self.timer.count = 0
                self.timer.end = self.interval
            sender.title = self.config["pause"]
            self.timer.start()
        else:
            sender.title = self.config["continue"]
            self.timer.stop()

    def stop_timer(self, sender=None):
        self.set_up_menu()
        self.stop_button.set_callback(None)
        self.set_button.set_callback(self.set_timer)
        self.setMessage_button.set_callback(self.set_message)
        self.start_pause_button.title = self.config["start"]

    def set_timer(self, sender):
        
        self.interval = 20
        self.set_up_menu()

    def set_message(self, sender):
        self.break_message = "This is another break message, time's up."
        self.set_up_menu()

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = TimerTasticApp()
    app.run()
    
