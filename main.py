import turtle
from paddle import Paddle
from ball import Ball
from Button import Button
from scoreboard import Scoreboard
import time as t

# Setup Screen
main_screen = turtle.Screen()
main_screen.setup(600, 600)
main_screen.bgcolor("black")
main_screen.title("Tim's Wacky Pong")
main_screen.tracer(0)

def exit_program():
    turtle.bye()

# Setup Paddles
player_paddle = Paddle()
player_paddle.goto(-270, 0)
player_paddle.setheading(90)

enemy_paddle = Paddle()
enemy_paddle.goto(270, 0)
enemy_paddle.setheading(90)

# Setup Rest
ball = Ball()
scoreboard = Scoreboard()

# Variables to track key states
player_key_pressed = {"W": False, "S": False}
enemy_key_pressed = {"Up": False, "Down": False}

def on_key_press(key, player):
    player[key] = True  # Set key state to True when pressed

# Function to handle key release
def on_key_release(key, player):
    player[key] = False  # Set key state to False when released

# Checks if keys are pressed or released
# Player controls (left paddle)
main_screen.onkey(lambda: on_key_press("W", player_key_pressed), "w")  # Bind W key press
main_screen.onkey(lambda: on_key_release("W", player_key_pressed), "W")  # Bind W key release
main_screen.onkey(lambda: on_key_press("S", player_key_pressed), "s")  # Bind S key press
main_screen.onkey(lambda: on_key_release("S", player_key_pressed), "S")  # Bind S key release

# Enemy controls (right paddle)
main_screen.onkey(lambda: on_key_press("Up", enemy_key_pressed), "Up")  # Bind Up key press
main_screen.onkey(lambda: on_key_release("Up", enemy_key_pressed), "Up")  # Bind Up key release
main_screen.onkey(lambda: on_key_press("Down", enemy_key_pressed), "Down")  # Bind Down key press
main_screen.onkey(lambda: on_key_release("Down", enemy_key_pressed), "Down")  # Bind Down key release

# Checks if player has exited the game
main_screen.onkeypress(exit_program, "Escape")
main_screen.listen()

main_screen.onkeypress(ball.reset, "1")

# Number of players and if game is running
state = {'players': 0, 'game_playing': False}

# Hides buttons, sets players and starts game
def player_clicked(button, p1, p2, state):
    state['players'] = button
    state['game_playing'] = True
    p1.clear()
    p1.ht()
    p2.clear()
    p2.ht()

# Creates P1 and P2 buttons
p1_button = Button()
p1_button.write_text("P1")
p2_button = Button()
p2_button.write_text("P2")

p1_button.onclick(lambda x, y: player_clicked("1", p1_button, p2_button, state))
p2_button.onclick(lambda x, y: player_clicked("2", p1_button, p2_button, state))

# Keeps game running if not playing
while state['game_playing'] == False:
    main_screen.update()

# Runs main game loop
while state['game_playing'] == True:
    t.sleep(0.01)
    ball.move()
    main_screen.update()
    player_paddle.paddle_boundary()
    enemy_paddle.paddle_boundary()

    if player_key_pressed["W"]:
        player_paddle.up()
    if player_key_pressed["S"]:
        player_paddle.down()

    if enemy_key_pressed["Up"]:
        enemy_paddle.up()
    if enemy_key_pressed["Down"]:
        enemy_paddle.down()

    if (player_paddle.distance(ball) < 60 and ball.xcor()) < -250 or (enemy_paddle.distance(ball) < 60 and ball.xcor() > 250):
        ball.hit_paddle()

    if ball.ycor() > 275:
        ball.hit_wall("top")
    elif ball.ycor() < -275:
        ball.hit_wall("bottom")

    if ball.xcor() > 271 or ball.xcor() < -271:
        if ball.xcor() > 285:
            winner = "enemy"
        else:
            winner = "player"
        scoreboard.increase_score(winner)
        player_paddle.goto(-270, 0)
        enemy_paddle.goto(270, 0)
        ball.reset(winner)
        t.sleep(0.8)

    if ball.xcor() > 125 and state['players'] == "1":
        enemy_paddle.enemy_tracking(ball)

    if scoreboard.score[0] == 7 or scoreboard.score[1] == 7:
        if scoreboard.score[0] == 7:
            scoreboard.game_win()
        elif scoreboard.score[1] == 7:
            scoreboard.game_lose()
        state['game_playing'] = False

    if scoreboard.score[0] - scoreboard.score[1] >= 2 and state['players'] == 1:
        enemy_paddle.speed = 10

turtle.done()


