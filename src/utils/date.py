from datetime import date, timedelta

def daterange(start_date : date, end_date : date):
    weekend = set([5, 6])
    for n in range(int((end_date - start_date).days)):
        day = start_date + timedelta(n)
        if day.weekday() in weekend:
            continue
        yield day
