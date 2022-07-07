def find_date_time(num_sec):
    # setting the default time to epoch
    epoch = '01-01-1970'
    # if the number of seconds is 0 then the time is epoch 01-01-1970
    if num_sec < 86400:
        date = epoch
    # if the number of seconds is greater than epoch the month, day and year are calculated
    else:
        total_days = nstockfleth_find_days(num_sec)
        year = nstockfleth_find_year(total_days)[0]
        days_in_current_year = nstockfleth_find_year(total_days)[1]
        month = nstockfleth_find_month(days_in_current_year, year)[0]
        day_of_month = nstockfleth_find_month(days_in_current_year, year)[1]
        date = nstockfleth_format_date(month, day_of_month, year)

    return date


def nstockfleth_find_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def nstockfleth_find_days(num_sec):
    days = num_sec // 86400
    return days


def nstockfleth_find_year(days):
    year = 1970
    while days >= 365:
        leap = nstockfleth_find_leap_year(year)
        if leap:
            if days - 366 < 0:
                break
            else:
                days -= 366
        else:
            if days - 365 < 0:
                break
            else:
                days -= 365

        year += 1
    days_into_current_year = days + 1
    return year, days_into_current_year


def nstockfleth_find_month(days_into_current_year, year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 0
    index = 0
    leap = nstockfleth_find_leap_year(year)
    if leap:
        months[1] = 29
    while days_into_current_year - months[index] > 0:
        days_into_current_year -= months[index]
        index += 1
        month += 1

    month += 1

    if month == 2 and days_into_current_year == 29:
        if not leap:
            days_into_current_year -= 28
            month += 1

    day_of_month = days_into_current_year
    return month, day_of_month


def nstockfleth_format_date(month, day, year):
    if month < 10:

        mm = '0' + str(month)
    else:
        mm = str(month)
    if day < 10:
        dd = '0' + str(day)
    else:
        dd = str(day)
    date = mm + '-' + dd + '-' + str(year)
    return date
