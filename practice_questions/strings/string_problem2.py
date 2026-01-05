# replace in a given string by user details and todays date 
from datetime import date
letter = ''' dear <|name>|
                you are selected
                <|date|>'''

print(letter.replace("<|name>|","Anobhav").replace("<|date|>",str(date.today())))