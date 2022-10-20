import re


class Email:
    e_type = "email"

    def __init__(self, email_address, email_length):
     self.email_address = email_address
     self.email_length = email_length

Harry = Email("harry55@gmail.com", 17) # email and email length in characters
print(Harry.email_address)

print(Harry.e_type)

subject = "jackmadden782@gmail.com"
pattern1 = "@"
pattern2 = ".com"
pattern3 = ".mail"
pattern4 = "$~:{0}"
match_obj1 = re.search(pattern1, subject)
match_obj2 = re.search(pattern2, subject)
match_obj3 = re.search(pattern3, subject)
match_obj4 = re.search(pattern4, subject)
print(match_obj1)
print(match_obj2)
print(match_obj3)
print(match_obj4)

class ValidEmail:

 def __init__(self):
     pass
def is_it_a_valid_email(self,subject):
    """
    Search for a pattern within an email address. Uses Regex expressions with re.search
"""
subject = "jackmadden782@gmail.com"
pattern1 = "@"
pattern2 = "[.com.mail]{1}"
pattern3 = "$~:{0}"
match_obj1 = re.search(pattern1, subject)
match_obj2 = re.search(pattern2, subject)
match_obj3 = re.search(pattern3, subject)
print(match_obj1)
print(match_obj2)
print(match_obj3)

email_validator = ValidEmail()
email_validator.is_it_a_valid_email("Incorrect")


#class Gmail(Email):
