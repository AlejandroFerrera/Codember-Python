import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from utils.utils import get_text_data, save_text_data

TEXT_URL = 'https://codember.dev/data/message_01.txt'






if __name__ == '__main__':
    
	TEXT_DATA = get_text_data(TEXT_URL)
	TEXT_FILE_NAME = 'message_01.txt'
	save_text_data(TEXT_DATA, TEXT_FILE_NAME)


