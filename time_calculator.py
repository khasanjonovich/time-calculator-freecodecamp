def add_time(s, d, week_day=""):

    sh, sm = clear_data(s, True)
    dh, dm = clear_data(d)

    hours, minutes, time_format= calculate_time(sh, sm, dh, dm)
    calculated_weekday, days = calculate_days(sh, sm, dh, dm)

    output = '%d:%02d %s' %(hours, minutes, time_format)
    if week_day !="":
        week_day = calculate_week(week_day, calculated_weekday)
        output = output + ", %s" %(week_day.title())
    if calculated_weekday != 0:
        output = output + " (%s)" %(days)

    return output


def clear_data(start, arg=False):
    h, m = start.split(":")
    h = int(h)
    m = int(m[:2])

    if arg and start.split()[1] == "PM":
        return h + 12, m

    return h, m


def calculate_time(*args):
    sh, sm, dh, dm = args
    # print start time in 24-hour format
    print(args)


    minutes = (sm + dm) % 60
    hours = ((sm+dm) // 60 + sh + dh) % 24

    if hours > 12:
        return hours - 12, minutes, "PM"
    elif hours == 12:
        return hours, minutes, "PM"
    elif hours == 0:
        return hours + 12, minutes, "AM"

    return hours, minutes, "AM"

def calculate_days(*args):
    sh, sm, dh, dm = args

    days = ((sm + dm) // 60 + sh + dh) // 24

    if days == 1:
        return days, "next day"
    elif  days > 1:
        return days, f"{days} days later"
    else:
        return days, ""


def calculate_week(given, calculated):

    given = given.title()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    index = days.index(given) + 1

    return days[(index+calculated) % 7 - 1]
