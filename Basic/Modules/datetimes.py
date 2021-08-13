from datetime import datetime

bithday = datetime(1992, 10, 4, 5, 15, 23)

bithday.year

bithday.day

bithday.month

# TERMINAL
# % python3
# >>> from datetime import datetime
# >>> bithday = datetime(1992, 10, 4, 5, 15, 23)
# >>> bithday.year
# 1992
# >>> bithday.month
# 10
# >>> datetime.now()
# datetime.datetime(2021, 8, 2, 14, 42, 20, 677498)
# >>> datetime.now() - datetime(1992,10,4)
# datetime.timedelta(days=10529, seconds=53139, microseconds=722545)
# >>> parsed_date = datetime.strptime("Jan 01, 2019", "%b %d, %Y")
# >>> parsed_date.year
# 2019
# >>> date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
# >>> date_string
# 'Aug 02, 2021'

# LEARNING PIPENV

# exit() to finish the python terminal