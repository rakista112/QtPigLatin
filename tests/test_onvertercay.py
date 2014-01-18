import unittest
from wordplay.onvertercay import OnverterCay

class TestOverterCay(unittest.TestCase):
	def setUp(self):
		self.onverterCay = OnverterCay()
		self.testWord = 'test'
		self.expectedResult = 'est-tay'
	
	def test_onvertCaying(self):
		result = self.onverterCay.onvertCay(self.testWord)
		self.assertEqual(self.expectedResult, result, 'oh this ain\'t right...')
		
