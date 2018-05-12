import unittest
import cap_test

class TestCap(unittest.TestCase):

	def test_one_world(self):
		text="python"
		result=cap.cap_test()
		self.assertEqual(result,'Python')

	def test_multiple_word(self):
		text = 'monty python'
		result = cap.cap_test(text)
		self.assertEqual(result,'Monty Python')

if __name__=='__main__':
	unittest.main()