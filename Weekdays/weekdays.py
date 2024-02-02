from datetime import timedelta


WORKDAY = 8


def weekdays(start, end):
    """
    Parameters start and end are date objects.
    Return amount of working hours between
    start and end days. Weekdays (Mon, Tue, Wed, Thu, Fri)
    are counted as working days and one workday is 8 hours long.
    """
    result = []
    if start > end:
        return 0
    current = start
    oneday = timedelta(days=1)

    while True:
        if current.weekday() < 5:
            result.append(current)
        if current >= end:
            return len(result) * WORKDAY
        current = current + oneday
