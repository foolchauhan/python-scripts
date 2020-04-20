# Timer App for Mac - TimerTastic
This timer app will be a menubar app to run on mac.

# Functionalities
- Run timer with miliseconds on menubar
- When not running, show one icon for it
- Click on menubar icon/time-runner for options
- Options available - Stop, Set timer, Quit, Set message
- On completion of time show a notification with sound and change backto icon from timer
- Provide some default messages
- Prepare a standalone app for this

# Tech Stack to be used
1. Python3
2. Rumps
3. py2app (for making standalone app)

# Considerations while development
1. Always use virtual environments
2. Use python3 and pip3
3. Update on git regularly
4. Update any new ideas or tech stack used on this file

# For Developers
run this to create app
```
python3 setup.py py2app
```
The file should be present in dist folder created (possibly **dist/TimerTastic.app/Contents/MacOS/**)

