from venue import Venue
from enum import Enum
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