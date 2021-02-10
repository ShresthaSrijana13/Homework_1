# Srijana Shrestha
# 1918305

# importing date from datetime function
from datetime import date

# printing a headline
print("***Birthday Calculator***")
print('-'*25)

# printing current date
current_date = str(date.today())
print("Current_date:", current_date)

# assigning variables for year, month and day. Convert the string into integer
c_year = int(current_date[:4])
c_month = int(current_date[5:7])
c_day = int(current_date[8:10])


print("Birthday")
b_month = int(input('Month:'))
b_day = int(input("Day:"))
b_year = int(input("Year:"))

if b_year > c_year:
    print('Invalid date!!!')
elif b_year == c_year:
    print('0 years old!!!')
else:
    year = (c_year - b_year) * 365
    month = (c_month - b_month) * 30
    days = (c_day - b_day)
    calculatedYears = int((year + month + days)/365)
    print('You are', calculatedYears, 'years old.')

if c_day == b_day and c_month == b_month:
    print("Happy Birthday!")
