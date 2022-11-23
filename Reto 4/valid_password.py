def is_valid_password(password: int) -> bool:
    
    code = str(password)
    if len(code) != 5:
        return False

    for i in range(1, len(code)):

        if code[i] < code[i - 1]:
            return False
        
        if code.count('5') < 2:
            return False
        
    return True


valid_passwords = [number for number in range(11098, 98124) if is_valid_password(number)]

print(f"{len(valid_passwords)}-{valid_passwords[55]}")


        



 
# 55678 is correct, it fulfills everything
# 12555 is correct, it fulfills everything
# 55555 is correct, it fulfills everything
# 12345 is incorrect, it does not have the 5 repeated.
# 57775 is incorrect, the numbers do not go in increasing order
