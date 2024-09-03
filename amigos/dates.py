from datetime import datetime
from datetime import date

now = datetime.now()
print(now)
# print(datetime.now().date())
# print(datetime.now().hour)
# print(datetime.now().year)
# print(datetime.now().day)
# print(date.today())

print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))






