import re
from collections import deque

phone_regex = re.compile(r'^01[0-9]{8,11}$')

print(phone_regex.match('01011112222') != None)
