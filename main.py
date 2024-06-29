# TO GET COLOR LIST
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
color_list = [(224, 230, 235), (223, 234, 230), (235, 228, 210), (60, 104, 143), (216, 151, 81), (128, 91, 61), (238, 225, 234), (221, 201, 117), (145, 176, 198), (191, 144, 169), (140, 76, 99), (208, 92, 65), (69, 109, 89), (134, 178, 137), (185, 84, 113), (43, 156, 185), (70, 154, 94), (148, 133, 77), (14, 50, 87), (183, 191, 203), (30, 64, 111), (64, 50, 39), (215, 178, 196), (123, 39, 49), (116, 119, 150), (170, 207, 185), (44, 61, 56), (79, 36, 50), (233, 173, 164), (162, 208, 215)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
       tim.dot(20, random.choice(color_list))
       tim.forward(50)

       if dot_count % 10 == 0:
           tim.setheading(90)
           tim.forward(50)
           tim.setheading(180)
           tim.forward(500)
           tim.setheading(0)
           tim.hideturtle()


screen = turtle_module.Screen()
screen.exitonclick()