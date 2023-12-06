import sys
import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from utils.utils import get_text_data, save_text_data

class Attribute:

    @staticmethod
    def is_valid_id(user_id: str) -> bool:
        return user_id.isalnum()

    @staticmethod
    def is_valid_username(username: str) -> bool:
        return username.isalnum()

    @staticmethod
    def is_valid_email(email: str) -> bool:
        regex = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')
        return bool(re.match(regex, email))

    @staticmethod
    def is_valid_age(age: str) -> bool:
        return age.strip() == '' or age.isdigit()

    @staticmethod
    def is_valid_location(location: str) -> bool:
        return location.strip() == '' or location.isalpha()

def extract_invalid_usernames(users_list: list) -> str:
    return ''.join(user_data.split(',')[1][0] for user_data in users_list if not is_valid_user(user_data))

def is_valid_user(user_data: str) -> bool:
	_, username, email, age, location = user_data.split(',')

	print(f"{_ =}, {username=}, {email=}, {age=}, {location=}")
	return all([
	Attribute.is_valid_id(_),
	Attribute.is_valid_username(username),
	Attribute.is_valid_email(email),
	Attribute.is_valid_age(age),
	Attribute.is_valid_location(location)
	])

if __name__ == '__main__':
    TEXT_DATA = get_text_data('https://codember.dev/data/database_attacked.txt', is_url=True)
    USERS_LIST = TEXT_DATA.split('\n')

    invalid_usernames = extract_invalid_usernames(USERS_LIST)
    print(invalid_usernames)
