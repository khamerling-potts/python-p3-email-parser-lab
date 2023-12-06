# your code goes here!
import re


class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        email_regex = re.compile(r"[A-z]\.?([A-z\d]+\.?)*@[A-z\d]+\.[A-z\d]+")
        array = re.split(r",| ", self.addresses)
        parsed_set = set()
        for email in array:
            if email_regex.fullmatch(email):
                parsed_set.add(email)
        return sorted(list(parsed_set))
