from responses import responses
from datetime import datetime

def get_jarvis_reply(message):

    message = message.strip().lower()

   
    if "date" in message:
        return datetime.now().strftime("%I:%M %p")

    if "time" in message:
        return datetime.now().strftime("%d-%m-%Y")
    return responses.get(
    message,
    "Sorry, I don't understand that command yet."
)