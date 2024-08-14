from turtle import Screen
import time  # time function creates delay for our code
from player import Player
from bullet import Bullets

screen = Screen()
screen.tracer(0)  # very important since it updates the code every time
screen.setup(400, 600)

player = Player()
bullets_attack = Bullets()
screen.listen()  # allows computer to listen to your keys(on keys)
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")
screen.onkeypress(player.right_1, 'Right')
screen.onkeypress(player.left_1, "Left")

i = True  # allows while loop to continue
while i:
    bullets_attack.background_color_change(screen)
    time.sleep(0.1)  # slow down the code
    screen.update()  # goes with tracer(0) function
    bullets_attack.create()
