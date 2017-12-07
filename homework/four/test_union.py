import unittest
from union import Union
class TestVenue(unittest.TestCase):
	def setUp(self):
		self.union = Union()
	def test_check_get_venue_list(self):
		self.assertTrue( len(self.union.get_venue_list()) > 0)


if __name__ == '__main__':
    unittest.main()