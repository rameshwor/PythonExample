### Unit Test Cases for Roman Program ###
## every test is its own method, method name must start with 'text' 

## Methods whose names start with the string test with one argument (self) 
## in classes derived from unittest.TestCase are test cases
import roman1
import unittest

class knownValues(unittest.TestCase):
	known_values = ((1,'I'),(100,'C'))

	def test_to_roman_known_values(self):
		''' to_roman should give known result with known input'''
		for integer,numeral in self.known_values:
			result=roman1.to_roman(integer)
			self.assertEqual(result,numeral)

if __name__ == '__main__':
		unittest.main()


