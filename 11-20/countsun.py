import datetime


def count_sunday(startyear, endyear):

    total = 0

    start = datetime.date(year=startyear, month=1, day=1)
    end = datetime.date(year=endyear, month=12, day=31)

    def daterange(start_date, end_date):
        for n in range(int((end_date-start_date).days)):
            yield start_date + datetime.timedelta(n)

    def check_day(date):

        day = date.day

        if date.month > 2:
            month = date.month - 2
            year = str(date.year)
        else:
            month = date.month + 10
            year = str(date.year - 1)

        century = int(year[:2])
        year = int(year[2:])

        interim = day + int((13 *  month - 1)/5) + year + int(year/4) + int(century/4) - 2*century

        return interim % 7

    for i in daterange(start, end):
        print(check_day(i))
        if i.day == 1 and check_day(i) == 0:
            total += 1

    return total

print(count_sunday(1901, 2000))
