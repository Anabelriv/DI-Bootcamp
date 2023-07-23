import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Ask the user for their birthdate (format: DD/MM/YYYY)
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

# Extract the year from the birthdate
year = int(birthdate[-4:])

# Check if the birth year is a leap year
leap_year = is_leap_year(year)

# Calculate the age and the number of candles
current_year = datetime.datetime.now().year
age = current_year - year
last_digit_age = age % 10
num_candles = last_digit_age

# Display the cake with candles
cake = f"""
       ___{'i' * (len(str(last_digit_age)))}____
      |:H:a:p:p:y:|
    __|{'_' * 11}|__
   |{'^' * 15}|
   |:B:i:r:t:h:d:a:y:|
   |{' ' * 17}|
   ~~~~~~~~~~~~~~~~~~~
"""

print(cake)

# Bonus: Display two cakes if born on a leap year
if leap_year:
    print(cake)
