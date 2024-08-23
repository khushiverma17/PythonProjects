
import turtle
import random
import time




# creating screen
screen = turtle.Screen()
screen.title("Snake Game", )
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# creating border
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color("red")
border.forward(600)
border.right(90)
border.forward(500)
border.right(90)
border.forward(600)
border.right(90)
border.forward(500)
border.penup()
border.hideturtle()

# screen.update()
# screen.mainloop()

score = 0;
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.forward(3)
snake.direction = "stop"

# creating food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

old_fruit = [] # eaten fruit will be added in it

#scoring
scoring = turtle.Turtle()
scoring.speed(60)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))

# define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        y=snake.ycor() # xcor and ycor returns the current coordinates of the turtle
        snake.sety(y+20)

    if snake.direction == "down":
        y=snake.ycor() # xcor and ycor returns the current coordinates of the turtle
        snake.sety(y-20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


#keyboard binding
screen.listen()
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_right, "Right")
screen.onkeypress(snake_go_down, "Down")

#main loop

while True:
    screen.update()

    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score+=1
        scoring.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))
        delay -= 0.001 # delay is used to speed up the snake after eating the fruit

        # creating new fruit
        new_fruit = turtle.Turtle()
        new_fruit.shape("square")
        new_fruit.speed(0)
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    #adding to snake
    for index in range(len(old_fruit)-1, 0, -1):
        a = old_fruit[index-1].xcor()
        b = old_fruit[index-1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()

    # collision with border
    if snake.xcor() > 290 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write(f"Score: {score}")
        time.sleep(3)
        break

    # collision with its body
    for food in old_fruit:
        if food.distance(snake) < 20:

            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(f"Score: {score}")
            time.sleep(3)
            break

    time.sleep(delay)

turtle.Terminator()