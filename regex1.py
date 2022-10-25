import re


def validate(username):
    """""
    # username is >= to 4 characters
    # username starts with a letter- ^[A-Z-a-z]
    # contains only letters or numbers - [A-Z-a-z0-9]*
    # Can only have one underscore - [_]?
    # Does not end with an underscore -[A-Z-a-z]$ """

    if re.match('^\w[^\s]{4,}[^_$]', username):
        return True
    else:
       return False


print(validate("Mike_Standish"))  # Valid username
print(validate("Mike Standish"))  # Invalid username
