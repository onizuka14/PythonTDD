from django.test import TestCase

class SmokeTest(TestCase):
	
	def test_bad_mathes(self):
		self.assertEqual(1 + 1, 3)