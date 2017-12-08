from venue import Venue
from venue_request import Venue_Request, Activity
from union import Union
import calendar
from datetime import datetime,timedelta
class Request_System:
    union = Union()
    request_indexer = 0
    accepted_venue_requests = []
    pending_venue_requests = []

    def __init__(self):
        pass

    def approve_request(self, request_id):
        for m in self.pending_venue_requests:
            if request_id == m.id:
                self.accepted_venue_requests.append(m)
                self.pending_venue_requests.remove(m)
                return "Approved request: {}".format(request_id)
            return "Error processing request"

    def convert_text_to_date(self, date):
        try:
            return datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            return datetime.now()

    def free_rooms(self, date_text):
        date = self.convert_text_to_date(date_text)
        rooms = self.union.get_venue_list()
        not_free = [
            m.name for m in self.accepted_venue_requests
            if m.start > date and m.end < date
        ]
        if date_text != None or date_text.strip() != "" or date_text != '%2':
            temp = "Rooms free on {}:\n".format(date)
        else:
            temp = ""
        for m in [r for r in rooms if r not in not_free]:
            temp += "{}\n".format(m)
        return temp

    def submit_request(self,venue, start, end, activity):
        if self.check_venue(venue, start, end):
            self.request_indexer += 1
            ven_req = Venue_Request(self.request_indexer,
                                    venue,
                                    start,
                                    end,
                                    activity)
            self.pending_venue_requests.append(ven_req)
    def check_venue(self,venue, start, end):
        not_free = [
            m for m in self.accecpted_venue_requests
            if m.start < start and m.end > end and m.venue == venue
        ]
        return len(not_free) == 0
    def view_request(self):
        result = "Pending Requests:\n"
        for m in self.pending_venue_requests:
            result+="Venue:{}\tStart:{}\tEnd:{}".format(m.venue.name, m.start,m.end)
