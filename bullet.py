from turtle import Turtle
import random

starting_movement = 5
letters_and_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', "E", 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Bullets:

    def __init__(self):
        self.bullets = []  # manage the bullets
        self.color = '#CD5C5C'
        self.level = 1

    def create(self):
        new = Turtle("square")
        new.penup()
        new.shapesize(stretch_wid=2, stretch_len=1)
        new.color(self.color)
        y_coordinate_on_screen = random.randint(-250, 250)
        new.goto(200, y_coordinate_on_screen)
        self.bullets.append(new)

    def background_color_change(self, screen):
        s = 7 - self.level
        color_bg = self.color
        index = 0
        for x in color_bg:
            if index == s:
                replaced_color = color_bg.replace(x, random.choice(letters_and_numbers))
            index += 1
        screen.bgcolor(replaced_color)
