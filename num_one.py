from datetime import date


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

date = date(year, month, day)


def user_date():
	x = str(date).split("-")
	y = '/'.join(x)
	userDate = ''.join(x)
	# Standard Date format year-month-day
	# print(date)
	print(f"Standard Date Format {date}")

	# formatted date in the form year/month/day
	# print(y)
	print(f"Formatted Date with Slashes {y}")

	# API date format in the form YYYYMMDD
	# print(userDate)
	print(f"API Date format {userDate}")


user_date()