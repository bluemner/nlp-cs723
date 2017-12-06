# hugotbot.py
from nltk.chat.util import Chat, reflections

# Need a room regex 
need_room_regex = r'(.*)(need a room)'

def room_request_process:
    # state 


def room_info():
    return "Here is the room info"
command_list = '''
               Welcome to the room request utility
               Can I help you will the following:
                    * Request a room
                    * Cancel a request
                    * View information about a request
                    * Room information
               '''
def help(name):
    return 
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