import unittest
from venue import Venue
class TestVenue(unittest.TestCase):
	def setUp(self):
		self.venue_00 = Venue(0,"Test",100)
		self.venue_01 = Venue(1,"Test",100)
	def test_check_eq(self):
		self.assertTrue(self.venue_00 == self.venue_00)
	def test_check_ne(self):
		self.assertTrue(self.venue_00 != self.venue_01)
if __name__ == '__main__':
    unittest.main()