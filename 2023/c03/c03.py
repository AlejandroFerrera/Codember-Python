import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from utils.utils import get_text_data, save_text_data

def valid_keys(keys:list) -> int:
	"""
		Returns the number of valid keys in the given list of keys.
		Args:
			keys (list): The list of keys to check.
		Returns:
			int: The number of valid keys in the given list of keys.
	"""
	counter = 0
	result = ''

	for key in keys:
		if not _is_valid_key(key):
			counter += 1
		if counter == 42:
			result = key
	
	return ( counter, result )

def _is_valid_key(key:str) -> bool:
	"""
		Returns True if the given key is valid, False otherwise.
		Args:
			key (str): The key to check.

		Returns:
			bool: True if the given key is valid, False otherwise.
	"""
	#Split the key into its components
	min_count = int(key.split('-')[0])
	max_count = int(key.split('-')[1].split(' ')[0])
	letter = key.split(' ')[1][0]
	password = key.split(' ')[2]

	#Check if the password is valid
	letter_count = password.count(letter)
	is_valid = min_count <= letter_count <= max_count

	return is_valid


if __name__ == "__main__":
	text_data = get_text_data('https://codember.dev/data/encryption_policies.txt', is_url=True)
	text_data = text_data.split('\n')

	print(valid_keys(text_data))