#######################################################################
#Exercise 16.1
#######################################################################


class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Adds two time objects.

    t1, t2: Time

    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def mul_time(time, factor):
    """Multiplies a Time object by a number and returns a new Time object.

    time: Time object
    factor: float

    returns: Time object
    """
    total_seconds = time_to_int(time)
    multiplied_seconds = total_seconds * factor
    return int_to_time(int(multiplied_seconds))


def average_pace(finishing_time, distance):
    """Calculates the average pace (time per mile).

    finishing_time: Time object
    distance: float

    returns: Time object representing the average pace
    """
    return mul_time(finishing_time, 1 / distance)


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Starts at', end=' ')
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    print_time(run_time)

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print('Ends at', end=' ')
    print_time(end_time)

    # Calculate the average pace
    finishing_time = Time()
    finishing_time.hour = 1
    finishing_time.minute = 30
    finishing_time.second = 0
    distance = 10  # miles

    print('Finishing time', end=' ')
    print_time(finishing_time)

    avg_pace = average_pace(finishing_time, distance)
    print('Average pace per mile', end=' ')
    print_time(avg_pace)


if __name__ == '__main__':
    main()
