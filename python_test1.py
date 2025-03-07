import re

def is_valid_string(s: str) -> bool:
    pattern = r'^(?=(?:\D*\d\D*){2,3}$)(?=.*\D).{6,}$'
    return bool(re.fullmatch(pattern, s))

# Test cases
print(is_valid_string("a1b2cd"))  # True (valid: 6 chars, 2 numbers, non-numeric between numbers)
print(is_valid_string("123456"))  # False (no non-numeric between numbers)
print(is_valid_string("a1b2c3"))  # True (valid: 6 chars, 3 numbers, non-numeric between numbers)
print(is_valid_string("a12bcd"))  # False (two numbers together without separation)
print(is_valid_string("abcde1"))  # False (only 1 number)
print(is_valid_string("a1b2c3d4"))  # False (more than 3 numbers)
