
import re
fields = ['usr','eme','psw','age','loc','fll']

def is_valid_user(user: str) -> bool:
    for field in fields:
        if user.find(field) == -1:
            return False
    return True

def get_user_name(user: str) -> str:
    username = re.findall('^usr:@[a-z]*', user)
    return username[0] if username else ''

with open("users.txt") as file:
    data = file.readlines()
    user = ''
    last_valid_user = ''
    valid_users = 0

    for line in data:
        if line != '\n':
            user += line
        else:
            if is_valid_user(user):
                valid_users += 1
                last_valid_user = user
            user = ''
    
print(valid_users, get_user_name(last_valid_user))
    

            

