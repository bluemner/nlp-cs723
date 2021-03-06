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
		
		self.req_sys.accepted_venue_requests.append(
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
		
		self.req_sys.accepted_venue_requests.append(
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
	def test_convert_text_to_date(self):
		actual = self.req_sys.convert_text_to_date('12/13/1992')
		expected = datetime.strptime('12/13/1992', "%m/%d/%Y")
		self.assertEqual(actual,expected)

		actual = self.req_sys.convert_text_to_date('1/1/2017')
		expected = datetime.strptime('01/01/2017', "%m/%d/%Y")
		self.assertEqual(actual,expected)
		 
	def test_convert_text_to_date_2_diget_year(self):
		actual = self.req_sys.convert_text_to_date('12/12/92')
		expected = datetime.strptime('12/12/92', "%d/%m/%y")
		self.assertEqual(actual,expected)
	def test_view_request(self):
		start = datetime.strptime('01/01/2018', "%d/%m/%Y")
		
		self.req_sys.accepted_venue_requests.append(
			Venue_Request(0,
				Union.venues[0],
				start,
				start + timedelta(hours=9),
				Activity.Exposition
			)
		)
		test = self.req_sys.view_request()
		self.assertTrue(test != 'Pending Requests:')

	def test_submit_request(self):
		start = datetime.strptime('01/01/2018', "%d/%m/%Y")
		before = len(self.req_sys.pending_venue_requests)
		self.req_sys.submit_request(	
				Union.venues[0],
				start,
				start + timedelta(hours=9),
				Activity.Exposition)
		end = len(self.req_sys.pending_venue_requests)
		self.assertTrue(before != end)
		self.assertTrue(before < end)
if __name__ == '__main__':
    unittest.main()