import re
from turtledemo.penrose import start

regex = r'\d{2}'

txt = 'Apple and banana are fruits. An old cliche 25 says an apple a day a doctor way has 2020 been replaced by a banana a day keeps the doctor far far away.'

match = re.findall(regex, txt)
print(match)