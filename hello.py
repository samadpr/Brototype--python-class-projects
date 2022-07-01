"""a = input("Enter 2 numbers")
b = input()

print("Hi, How are you?" + a + "    second value is " + b)

sum = int(a) + int(b)

print("result is "+str(sum))
"""

"""
name= 'abdul samad'

name='darul uloom'

values=["saalim", "saleem", "samad" ]

values=values + ["abdul samad", 10]

values.append(input("enter a value"))

print(values)
"""

"""
import if_sample
print(if_sample.__name__)

check=if_sample.checkNegOrPos
check(20)
"""

"""
from if_sample import checkNegOrPos

checkNegOrPos(10)
"""
"""
import if_sample as ifs

ifs.checkNegOrPos(-10)
"""

"""
from if_sample import checkNegOrPos as check

print("1st")
check(10)
print("2nd")
check(-10)
print("3rd")
check(9489)
print("4th")
check(-239)
"""
"""
import platform

print(platform.system())
"""

"""
import code

print(code)
"""


b=0
try:
    a=10/b
    print(a)
    print('try completed')
except ZeroDivisionError:
    print('enter other value')
    print("can't divided by zero")

print("program completed")
