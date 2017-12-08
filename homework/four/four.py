# hugotbot.py
from nltk.chat.util import Chat, reflections

import calendar
from datetime import datetime

from request_system import Request_System
from union import Union
from venue_request import Venue_Request
from venue import Venue

#############################

req_system = Request_System()

def room_info():
    return "Here is the room info"

def help(name):
    #need_room_regex = r'(.*)(need a room)'
    command_list = '''
    Welcome to the room request utility
    Can I help you will the following:
        * Request a room
        * Cancel a request
        * View information about a request
        * Room information
               '''
    return command_list
pairs = [
    [
        r'hi',
        ['hello', 'kamusta', 'mabuhay',],
        
    ],
    [
        r'bender',
        ['is great!']
    ],
    [
        r'(.*)(help|Help)',
        [
            help("%1 %2")
        ]
    ],
    [
        r'(.*)(room info+)',
        [
            room_info()
        ]
    ],
    [
        r'(.*)(available rooms|free rooms)(.*)',
        [
            req_system.free_rooms("%2")
        ]
    ],
    [r'(.*)(are you a robot.*)',
        ["No I am a meat popsicle"]
    ],
    [r'(.*)',
        ["It looks like some intern deleted the spreed sheet agin"]
    ]
    
]
def hugot_bot():
    print("Hi how can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    hugot_bot()	