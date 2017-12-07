from venue import Venue

class Union:
    venues=[]
    def __init__(self):
        self.venues.append(Venue(0,"Union Concourse",300))
        self.venues.append(Venue(1,"Union Ballroom",1500,False,2))
        self.venues.append(Venue(2,"Wisconsin Room",1500,False,3))
        self.venues.append(Venue(3,"Alumni Fireside Lounge",200))
        self.venues.append(Venue(4,"Art Gallery",300, limited_availability=True))
        self.venues.append(Venue(5,"Union Cinema",300, limited_availability=True))
        self.venues.append(Venue(6,"Ernest Spaights Plaza",300))
        self.venues.append(Venue(7,"Pangaea Mall",300))
        self.venues.append(Venue(8,"Other Outdoor",2000, in_door=False))
        meeting_rooms = [145,179,181,183,191,198,220,240,250,260,280,340,342,343,344,346,347]
        for i,m in enumerate(meeting_rooms):
            self.venues.append(Venue(i+9,m,6))
    def get_venue_list(self):
        return [m.name for m in self.venues ]
    def get_room_count(self):
        return len(venues)
