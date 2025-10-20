#######################################################################
#Exercise 16.2
#######################################################################

import datetime

'''
1. Use the datetime module to write a program that gets the current 
date and prints the day of the week.
'''

def print_current_day_of_week():
    # Get the current date
    current_date = datetime.datetime.now()
    # Get the day of the week
    day_of_week = current_date.strftime("%A")
    print(f"Today is {day_of_week}")

print_current_day_of_week()


'''
2. Write a program that takes a birthday as input and prints the user’s 
age and the number of days, hours, minutes and seconds until their next birthday.
'''

def calculate_age_and_next_birthday(birthday):
    # Get the current date and time
    now = datetime.datetime.now()
    # Calculate the age
    age = now.year - birthday.year
    # Check if the birthday has already occurred this year
    next_birthday = datetime.datetime(now.year, birthday.month, birthday.day)
    if next_birthday < now:
        next_birthday = datetime.datetime(now.year + 1, birthday.month, birthday.day)
        age += 1
    
    # Calculate the time until next birthday
    time_until_next_birthday = next_birthday - now
    
    print(f"Age: {age} years")
    print(f"Time until next birthday: {time_until_next_birthday}")

# Example usage
birthday = datetime.datetime(1990, 6, 15)
calculate_age_and_next_birthday(birthday)


'''
3. For two people born on different days, there is a day when one is twice as 
old as the other. That’s their Double Day. Write a program that takes two 
birthdays and computes their Double Day.
'''

def find_double_day(birthday1, birthday2):
    if birthday1 > birthday2:
        birthday1, birthday2 = birthday2, birthday1

    # Calculate the difference in days
    difference = birthday2 - birthday1
    double_day = birthday2 + difference

    print(f"The Double Day is: {double_day.date()}")

# Example usage
birthday1 = datetime.datetime(1990, 6, 15)
birthday2 = datetime.datetime(1992, 6, 15)
find_double_day(birthday1, birthday2)


'''
4. For a little more challenge, write the more general version that computes 
the day when one person is n times older than the other.
'''

def find_n_times_older_day(birthday1, birthday2, n):
    if birthday1 > birthday2:
        birthday1, birthday2 = birthday2, birthday1

    # Calculate the difference in days
    difference = birthday2 - birthday1
    n_times_older_day = birthday2 + difference / (n - 1)

    print(f"The day when one person is {n} times older than the other is: {n_times_older_day.date()}")

# Example usage
birthday1 = datetime.datetime(1990, 6, 15)
birthday2 = datetime.datetime(1992, 6, 15)
n = 2  # Double Day
find_n_times_older_day(birthday1, birthday2, n)