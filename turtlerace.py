import turtle
import random
from turtle import Turtle,Screen
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
bet=screen.textinput(title="Place a bet",prompt="Which turtle do you think will win the race? \n                         Enter the colour ")
print(f"You have placed your bet on {bet} colour turtle!")
colours=["red","yellow","blue","purple","black","violet"]
position=[-70,-40,-10,20,50,80]
turtles=[]
for i in range(6):
    tortoise=Turtle(shape="turtle")
    tortoise.color(colours[i])
    tortoise.penup()
    tortoise.goto(x=-230,y=position[i])
    turtles.append(tortoise)
if bet:
    is_race_on=True
while(is_race_on):
    for turtle in turtles:
        if(turtle.xcor()>230):
            is_race_on=False
            winning_turtle=turtle.pencolor()
            if(winning_turtle==bet):
                print(f"You have won the race. The {winning_turtle} turtle is the winner!")
            else:
                print(f"You have lost the race. The {winning_turtle} turtle is the winner!")
        distance=random.randint(0,10)
        turtle.forward(distance)
screen.exitonclick()