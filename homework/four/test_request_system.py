import unittest
from datetime import datetime, timedelta
from request_system import Request_System
from venue_request import Venue_Request, Activity
from venue import Venue
from union import Union 
class Test_Request_System(unittest.TestCase):
	def setUp(self):
		self.req_sys = Request_System()
	def test_check_bad_date_in_rage(self):
		start = datetime.strptime('01/01/2018', "%d/%m/%Y")
		
		self.req_sys.accecpted_venue_requests.append(
			Venue_Request(0,
			Union.venues[0],
			start,
			start + timedelta(hours=9),
			Activity.Exposition
			)
		)

		result = self.req_sys.check_venue(
			Union.venues[0],
			start + timedelta(hours=2),
			start + timedelta(hours=2.5)
			)
		self.assertFalse(result)
	def test_check_good_date_out_of_rage(self):
		start = datetime.strptime('01/01/2018', "%d/%m/%Y")
		
		self.req_sys.accecpted_venue_requests.append(
			Venue_Request(0,
			Union.venues[0],
			start,
			start + timedelta(hours=9),
			Activity.Exposition
			)
		)

		result = self.req_sys.check_venue(
			Union.venues[0],
			start + timedelta(hours=24),
			start + timedelta(hours=30)
			)
		self.assertTrue(result)

		
if __name__ == '__main__':
    unittest.main()