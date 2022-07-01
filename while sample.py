"""i = 1
while i <= 10:
    print(i)
    i = i + 1

else:
    print("Loop is finished")
"""


def triangle(s):
    a = s - 1

    for i in range(0, s):

        for j in range(0, a):
            print(end=" ")

        a = a - 1

        for j in range(0, i + 1):
            print("* ", end="")

        print("\r")


s = 10
triangle(s)

"""
def triangle(n):

    k = n - 1


    for i in range(0, n):


        for j in range(0, k):
            print(end=" ")


        k = k - 1


        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")


        print("\r")



n = 10
triangle(n)
"""
