# hugotbot.py
from nltk.chat.util import Chat, reflections
from enum import Enum
import calendar
from datetime import datetime
class Activity(Enum):
    Banquet = 1
    Concert = 2
    Conference = 3
    Lecture  = 4
    Exposition = 5
    Film_Screening = 6
    Dance_or_Party = 7
    Reception = 8
    Other = 9

class Venue:
    id = None
    name = ""
    capcity= -1
    limited_availability = False
    partition = 1
    in_door = True
    def __init__(self,id,name, capcity, limited_availability=False, partition =1, in_door =True):
        self.id = id
        self.name = name
        self.capcity = capcity,
        self.limited_availability = limited_availability
        self.partition
        self.in_door = in_door

    def __eq__(self,other):
        return self.id == other.id and self.name == other.name and self.capcity == other.capcity
    def __ne__ (self, other):
        return not self.__eq__(other)
class Union:
    venues=[]
    def __init__(self):
        self.venues.append(0,"Union Concourse",300)
        self.venues.append(1,"Union Ballroom",1500,False,2)
        self.venues.append(2,"Wisconsin Room",1500,False,3)
        self.venues.append(3,"Alumni Fireside Lounge",200)
        self.venues.append(4,"Art Gallery",300, limited_availability=True)
        self.venues.append(5,"Union Cinema",300, limited_availability=True)
        self.venues.append(6,"Ernest Spaights Plaza",300)
        self.venues.append(7,"Pangaea Mall",300)
        self.venues.append(8,"Other Outdoor",2000, in_door=False)
        meeting_rooms = [145,179,181,183,191,198,220,240,250,260,280,340,342,343,344,346,347]
        for i,m in enumerate(meeting_rooms):
            self.venues.append(i+9,m,6)
    def get_venue_list():
        return [m.name for m in venues ]
class Venue_Request:
    id = None
    venue = None
    start = None
    end   = None
    activity = None
    def __init__(self,id,venue,start,end, activity):
        self.id = id
        self.venue = venue
        self.start = start
        self.end = end
        self.activity = activity
    def __eq__(self,other):
        return self.venue == other.venue and self.start == other.start and self.end == other.end
    def __ne__ (self, other):
        return not self.__eq__(other)
class Request_System:
    union = None
    request_indexer =0
    accecpted_venue_requests=[]
    pending_venue_requests = []
    def __init__(self):
        union = Union()

    def approve_request(request_id):
        temp_request = Venue_Request()
        for m in pending_venue_requests:
            if request_id == m.id:
                accecpted_venue_requests.append(m)
                pending_venue_requests.remove(m)
                break
    def validate(date):
        try:
            return datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return datatime.datatime.now
    def free_rooms(date_text):
        date = validate(date_text)
        return [m for m in accecpted_venue_requests if m.start > date and m.end < date ]
        
    def submit_request():
        pass
    def check_venue(venue,start,end):
        pass
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
            req_system.free_rooms("%3")
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