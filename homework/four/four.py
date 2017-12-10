#!/usr/lib/python3
from nltk.chat.util import Chat, reflections

import calendar
from datetime import datetime

from request_system import Request_System
from union import Union
from venue_request import Venue_Request
from venue import Venue


req_system = Request_System()

MONTH_DAY_YEAR_REG =r'(0?[1-9]|1[0-2])(-|/|\.)(0?[1-9]|[12]\d|30|31)(-|/|\.)(\d{4}|\d{2})(\d*)'
REQUEST_ROOM_REG = r'(.*)(request)(room|venue)(\d+)('+MONTH_DAY_YEAR_REG+r')('+MONTH_DAY_YEAR_REG+')'
REQUEST_FREE_VENUE_DATE_REG =  r'(.*)?(venue|rooms|venues) (available|free|open|empty) (.*)?('+MONTH_DAY_YEAR_REG+')'
FREE_ROOM_DATE_REG =  r'(.*)?(available|free|open|empty) (venue|rooms|venues) ('+MONTH_DAY_YEAR_REG+')?'
EVENT_REG = r'(.*)?(event name|event)( is)?(.*)' #'(.*)?(event|event name) (is)(.*)'
START_DATE_REG=r'(.*)?(start)(.*)?('+MONTH_DAY_YEAR_REG+')'
END_DATE_REG=r'(.*)?(end)(.*)?('+MONTH_DAY_YEAR_REG+')'
#EVENT_REG = r'(.*)?(venue|room)( is)?(.*)'

# Actvitiy ::
ACTIVITY_LIST_REG = r'Banquet|Concert|Conference|Lecture|Exposition|Film Screening?|Dance|Party|Reception'
ACTIVITY_REG = r'(.*)?(Activity|activity)(.*)?('+ACTIVITY_LIST_REG+'|'+ACTIVITY_LIST_REG.lower()+')'
ACTIVITY_OTHER_REG = r'(.*)?(Activity|activity)( is)?(.*)?'

VENUE_LIST_REG = r'(((Union.)?Concourse)|(Union.)?Ballroom|(Art.)?Gallery|(Alumni.)?Fireside(.Lounge)?|(Wisconsin(.Room)?)|(Union.)?Cinema|(Ernest)(.Spaights.)?(Plaza)?|Plaza|Mall|Pangaea)'

VENUE_LIST_ROOMS_REG = r'(145|179|181|183|191|198|220|240|250|260|280|340|342|343|344|346|347)'
VENUE_REG = r'(.*)?(venue|room)(.)?('+VENUE_LIST_REG+'|'+VENUE_LIST_ROOMS_REG+'|'+VENUE_LIST_ROOMS_REG.lower()+')(.*)?'

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
        * state the name of your event :
            - My event is <something>
            - The event is <something>
        What is the name of your event?
    '''
    return command_list

current_start_date = None
current_end_date = None
current_activity = None
current_event_name = None
current_people = None
current_venue = None
def free_rooms(current_start_date):
    return req_system.free_rooms(current_start_date)
def missing_item():
    message = ""
    if current_start_date == None:
        message += "you are missing start date\n"
    if current_end_date == None:
         message +="you are missing end date\n"
    if current_activity == None:
         message +="you are missing activity\n"
    if current_event_name == None:
         message +="you are missing event name\n"
    if current_people == None:
         message +="you are missing number of people\n"
    if current_venue == None:
         message +="you are missing venue\n"
    return message

def parse_name(name):
    current_event_name = name
    return "Event name saved:"+name

# Start date logic
def parse_start_date(date_text):
    current_start_date = date_text  
   # free_rooms = req_system.free_rooms(current_start_date)    
    return "Start Date:{}".format(current_start_date)
def parse_end_date(date_text):
    current_end_date = date_text  
    return  "End Date:{}".format(current_end_date)
def parse_venus(text):
    return req_system.union.get_venue_by_name(text)
hi =   [r'hi',['hello', 'kamusta', 'mabuhay']]
bender =  [r'bender',['is great!']]
hlp=[ r'(.*)(help|Help)', [help("%1 %2")]]
request_room = [REQUEST_ROOM_REG,[parse_venue_request('%3','%4','%5','%6')]]
# start 01/02/2014
# Enter a start date
# Enter an end date 
# Enter a venue
# Ender 
# request venue date date activity
test = lambda x:req_system.free_rooms(x)
# KEY PART
pairs = [ hi,
          bender,
          hlp,
          request_room,
          [VENUE_REG, ['Room in request is : %4']],
          [FREE_ROOM_DATE_REG,[test("%4") ]],
          [START_DATE_REG,[parse_start_date("%4")]],
          [END_DATE_REG,[parse_end_date("%4")]],
          [EVENT_REG,[parse_name('%4')]],  
          [REQUEST_FREE_VENUE_DATE_REG,[req_system.free_rooms("%2")]],
          [ACTIVITY_REG,["Your activity : %4"]],
          [ACTIVITY_OTHER_REG , ["Your activity other: %4"]],
          [r'(.*)(are you a robot.*)', ["No I am a meat popsicle"]],
          [r'quit',["By"]],
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
            "ERROR: %0 does not exist. Bailing out, you are on your own. Good luck!",
            "No %0. What kind of mutant ninja machine is this?"
            ]
           ]
]

def main():
    print(help(""))
    chat = Chat(pairs, reflections,)
    chat.converse()
if __name__ == "__main__":
    main()