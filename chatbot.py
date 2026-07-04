from responses import responses
import webbrowser
from datetime import datetime
import subprocess
from voice import reply
apps = {
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "file explorer": "explorer",
    "command prompt": "cmd",
    "powershell": "powershell",
    "task manager": "taskmgr",
    "control panel": "control",
    "vscode":"code",
    "microsoft edge":"msedge",
    "control panel":"control",
    "snipping tool":"snippingtool"
}
OPEN_COMMANDS = ["open", "launch", "start", "run","execute"]
def handle_datetime(message):
    if "date" in message:
        return reply(datetime.now().strftime("%I:%M %p"))

    if "time" in message:
        return reply(datetime.now().strftime("%d-%m-%Y"))
def handle_web(message): 
    if "google" in message:  
        if message.startswith("search"):
            query = message.replace("google ", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
           
            return reply(f"Searching for {query}")
        else:
            webbrowser.open("https://www.google.com")
           
            return reply("Opening google")

        
    if "gmail" in message or "mail" in message:
        webbrowser.open("https://mail.google.com")
        
        return reply("Opening Gmails")
        
def handle_apps(message):
    for app_name, command in apps.items():
        if any(cmd in message for cmd in OPEN_COMMANDS) and app_name in message:
            subprocess.Popen(command, shell=True)
            
            return reply(f"Opening {app_name.title()}")

        

    return None


def get_jarvis_reply(message):

    message = message.strip().lower()
    reply = handle_datetime(message)
    if reply:
        
        return reply

    reply = handle_web(message)
    if reply:
        
        return reply

    reply = handle_apps(message)
    if reply:
        
        return reply

    

         

    return responses.get(
        message,
        " Sorry, I don't understand that command yet.")
