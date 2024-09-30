from turtle import *
import random

m = Turtle()

m.speed(0)
colors = ["Red", "Yellow", "Green", "Blue"]


def n():
    ls = []
    s = [0, 1, 2]
    ni = int(input("Number of Shape: "))
    for i in range(ni + 1):
        ls.append(i)

    li = [num for num in ls if num not in s]
    return li


def q():
    mlis = n()
    for a in mlis:
        m.color(random.choice(colors))
        for i in range(a):
            m.forward(100)
            m.right(360 / a)


q()

sr = Screen()
sr.exitonclick()


# Another type with same pattern and codes

# from turtle import *
# import random
#
# m = Turtle()
# m.speed(0)
# colors = ["Red", "Yellow", "Green", "Blue"]
#
#
# def q(n):
#     for a in range(3, n):
#         m.color(random.choice(colors))
#         for i in range(a):
#             m.forward(100)
#             m.right(360 / a)
#
#
# q(int(input("The number of shape: ")))
# sr = Screen()
# sr.exitonclick()
