from datetime import datetime
import pytz
from pytz import all_timezones
len(all_timezones) >= 500

print(pytz.country_names['US'])
tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("New York time:", datetime_NY.strftime("%H:%M:%S"))

print(pytz.country_names['GB'])
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))

# Current time in Germany for my friend Pascal Edouard
print(pytz.country_names['DE'])
tz_Berlin = pytz.timezone('Europe/Berlin')
datetime_Berlin = datetime.now(tz_Berlin)
print("Berlin time:", datetime_Berlin.strftime("%H:%M:%S"))


