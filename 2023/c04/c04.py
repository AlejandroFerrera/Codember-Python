import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from utils.utils import get_text_data, save_text_data

def find_real_file(index: int, text_data: str) -> str:
	"""
		Find the real file in the index position
	"""

	counter = 0

	for file in text_data.split('\n'):
		if is_real_file(file):
			counter += 1
		if counter == index:
			return file
	return 'Not found'


def is_real_file(file_name: str) -> bool:

	"""
		File name: xyzz33-xy
		Result: ✅ Real (The checksum is valid)
		File name: abcca1-ab1
		Result: ❌ Fake (The checksum should be b1, it's incorrect)
		File name: abbc11-ca
		Result: ❌ Fake (The checksum should be ac, the order is incorrect)
		Each line indicates the file name and its corresponding checksum, separated by a hyphen (-).
	"""

	char_counter = {}
	input, checksum = file_name.split('-')

	for char in input:
		if char in char_counter:
			char_counter[char] += 1
		else:
			char_counter[char] = 1

	generated_checksum = ''

	for key in char_counter.keys():
		if char_counter[key] == 1:
			valid_char = key
			generated_checksum += valid_char
	
	return generated_checksum == checksum


if __name__ == "__main__":
	TEXT_DATA = get_text_data('https://codember.dev/data/files_quarantine.txt', is_url=True)

	print(is_real_file('xyzz33-xy'))
	print(is_real_file('abcca1-ab1'))
	print(is_real_file('abbc11-ca'))

	print(find_real_file(33, TEXT_DATA))