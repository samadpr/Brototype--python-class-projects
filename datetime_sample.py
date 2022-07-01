import datetime

now = datetime.datetime.now()

print(now.strftime("%d:%m:%Y"))  # capital Y(2022) or small later y(22)

print(datetime.date.today().month)

x = datetime.datetime(year=2022, day=2, month=9)
y = datetime.datetime(year=2022, day=1, month=9)

dif = x - y
print(dif)

end = datetime.datetime.now()

difference = end - now

print(difference)
