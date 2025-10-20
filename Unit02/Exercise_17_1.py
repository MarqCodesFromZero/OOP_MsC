#######################################################################
#Exercise 17.1
#######################################################################


'''
Using Time2.py, change the attributes of Time to be a single integer 
representing seconds since midnight. Then modify the methods (and the 
function int_to_time) to work with the new implementation. You should 
not have to modify the test code in main. When you are done, the output 
should be the same as before.
'''

from __future__ import print_function, division

class Time:
    """Represents the time of day.
       
    attributes: seconds since midnight
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        hour: int
        minute: int
        second: int or float
        """
        self.seconds = hour * 3600 + minute * 60 + second

    def __str__(self):
        """Returns a string representation of the time."""
        return '%.2d:%.2d:%.2d' % (self.hours(), self.minutes(), self.remaining_seconds())

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.seconds

    def is_after(self, other):
        """Returns True if this time is after the other time; False otherwise."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.seconds + other.seconds
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        return int_to_time(self.seconds + seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        return self.seconds >= 0

    def hours(self):
        """Returns the hour part of the time."""
        return self.seconds // 3600

    def minutes(self):
        """Returns the minute part of the time."""
        return (self.seconds % 3600) // 60

    def remaining_seconds(self):
        """Returns the remaining seconds after hours and minutes."""
        return self.seconds % 60


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    return Time(0, 0, seconds)


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
