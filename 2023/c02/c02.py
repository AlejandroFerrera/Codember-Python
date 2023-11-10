import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from utils.utils import get_text_data, save_text_data


def mini_compiler(text_data:str) -> str:
	"""
	A mini compiler that takes in a string of text_data and performs operations based on the symbols in the string.

	Parameters:
	text_data (str): A string of symbols that represent operations to be performed.

	Returns:
	str: A string that represents the result of the operations performed on the input string.
	"""

	TASKS = {
		'#': lambda n: n + 1,  # increment by 1
		'@': lambda n: n - 1,  # decrement by 1
		'*': lambda n: n ** 2, # square
		'&': lambda s, n: s + str(n) # append current value to string 
	}

	n = 0
	s = ''
 
	for symbol in text_data:
		if symbol != '&':
			n = TASKS[symbol](n)
		else:
			s = TASKS[symbol](s, n)
	return s
	

if __name__ == '__main__':
	TEXT_DATA = get_text_data('message_02.txt', is_url=False)
	result = mini_compiler(TEXT_DATA)
	print(result)