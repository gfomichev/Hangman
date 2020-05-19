def check_email(string):
    return (' ' not in string) and ('@' in string) and (string.rfind('@') + 1 < string.rfind('.'))
