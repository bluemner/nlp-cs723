from nltk.chat.util import Chat, reflections

import calendar
from datetime import datetime

from request_system import Request_System
from union import Union
from venue_request import Venue_Request
from venue import Venue

req_system = Request_System()

YEAR_MONTH_DAY_REG =r'(0?[1-9]|1[0-2])(-|/|\.)(0?[1-9]|[12]\d|30|31)(-|/|\.)(\d{4}|\d{2})(\d*)'
reqest_room_reg = r'(.*)(request)(room|venue)(\d+)('+YEAR_MONTH_DAY_REG+r')('+YEAR_MONTH_DAY_REG+')'
requst_free_venue_date_reg =  r'(.*)?(venue|rooms|venues) (available|free|open|empty) (.*)?('+YEAR_MONTH_DAY_REG+')'
free_room_date_reg =  r'(.*)?(available|free|open|empty) (venue|rooms|venues) ('+YEAR_MONTH_DAY_REG+')?'

def parse_venue_request(venue,start,end,activity):
     venue_id = req_system.union.get_venue_by_name(venue)
     req_system.submit_request(venue_id,start,end,activity)
def help(name):
    #need_room_regex = r'(.*)(need a room)'
    command_list = '''
    Welcome to the venue request utility
    Can I help you will the following:
        * open rooms|venues <date>?
        * request venue, start, end, activity
        * Anything else to be insulted ;p




        Please enter an event name
    '''
    return command_list


current_start_date = None
current_end_date = None
current_activity = None
current_event_name = None
current_people = None
current_venu = None
def missing_item():
    missing = False
    if current_start_date == None:
        print("you are missing start date")
        missing |= True
    if current_end_date == None:
        print("you are missing end date")
        missing |= True
    if current_activity == None:
        print("you are missing activity")
        missing |= True
    if current_event_name == None:
        print("you are missing  event name")
        missing |= True
    if current_people == None:
        print("you are missing number of people")
        missing |= True
    if current_venu == None:
        print("you are missing venu")
        missing |= True
    return missing
def next_task():
   pass

hi =   [
        r'hi',
        ['hello', 'kamusta', 'mabuhay'],
        
    ]
bender =  [r'bender',['is great!']]
hlp=[ r'(.*)(help|Help)', [help("%1 %2")]]
request_room = [reqest_room_reg,[parse_venue_request('%3','%4','%5','%6')]]

# Enter a start date
# Enter an end date 
# Enter a venu
# Ender 

#  request venu date date activity

# KEY PART
pairs = [ hi,
          bender,
          hlp,
          request_room,
          [ free_room_date_reg,[ req_system.free_rooms("%2")]  ],
          [
              requst_free_venue_date_reg,[req_system.free_rooms("%2")]],
          [r'(.*)(are you a robot.*)', ["No I am a meat popsicle"]],
          #wild card
          [r'(.*)',
            ["It looks like some intern deleted the spreed sheet agin", 
            "maybe you should look at the 'help' command",
            "this is not the command you are looking for",
            "Where did you learn to type?",
            "You type like I drive.",
            "It can only be attributed to human error",
            "What, what, what, what, what, what, what, what, what, what?",
            "You do that again and see what happens...",
            "Speak English you fool --- there are no subtitles in this scene.",
            "Maybe if you used more than just two fingers...",
            "ERROR: Root device mounted successfully, %0 does not exist.\
             Bailing out, you are on your own. Good luck!",
            "No %0. What kind of mutant ninja machine is this?"
            ]
           ]
]

def main():
    print(help(""))
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    main()	