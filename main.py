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

# Quits Screen
def exit_program():
    turtle.bye()

# Setup Paddles
player_paddle = Paddle()
player_paddle.goto(-270, 0)
player_paddle.setheading(90)

enemy_paddle = Paddle()
enemy_paddle.goto(270, 0)
enemy_paddle.setheading(90)

# Setup Ball + Scoreboard
ball = Ball()
scoreboard = Scoreboard()
""""""
# Variables to track which keys are being pressed
player_key_pressed = {"Up": False, "Down": False}
enemy_key_pressed = {"w": False, "s": False}

# Function to handle key press
def on_key_press(key, player):
    player[key] = True  # Set key state to True when pressed

# Function to handle key release
def on_key_release(key, player):
    player[key] = False  # Set key state to False when released

main_screen.listen()

# Checks if keys are pressed or released
# Player controls (left paddle)
main_screen.onkeypress(lambda: on_key_press("Up", player_key_pressed), "Up")
main_screen.onkeyrelease(lambda: on_key_release("Up", player_key_pressed), "Up")
main_screen.onkeypress(lambda: on_key_press("Down", player_key_pressed), "Down")
main_screen.onkeyrelease(lambda: on_key_release("Down", player_key_pressed), "Down")

# Enemy controls (right paddle)
main_screen.onkeypress(lambda: on_key_press("w", enemy_key_pressed), "w")
main_screen.onkeyrelease(lambda: on_key_release("w", enemy_key_pressed), "w")
main_screen.onkeypress(lambda: on_key_press("s", enemy_key_pressed), "s")
main_screen.onkeyrelease(lambda: on_key_release("s", enemy_key_pressed), "s")

# Checks if player has exited the game
main_screen.onkeypress(exit_program, "Escape")
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

# Changes the player count on click
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

    # Moves the left paddle if the player is holding up or down
    if player_key_pressed["Up"]:
        player_paddle.up()
    if player_key_pressed["Down"]:
        player_paddle.down()

    # Moves the right paddle if the player is holding s or w
    if enemy_key_pressed["w"] and state['players'] == "2":
        enemy_paddle.up()
    if enemy_key_pressed["s"] and state['players'] == "2":
        enemy_paddle.down()

    # Deflects the ball if it hits the paddle
    if (player_paddle.distance(ball) < 60 and ball.xcor()) < -250 or (enemy_paddle.distance(ball) < 60 and ball.xcor() > 250):
        ball.hit_paddle()

    # Deflects the ball if it hits a top or bottom wall
    if ball.ycor() > 275:
        ball.hit_wall("top")
    elif ball.ycor() < -275:
        ball.hit_wall("bottom")

    # Gives a point and resets the ball if it hits a right or left wall
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

    # Gives enemy paddle AI if there are 1 players
    if ball.xcor() > 125 and state['players'] == "1":
        enemy_paddle.enemy_tracking(ball)

    # Increases AI speed if there is a score gap
    if scoreboard.score[0] - scoreboard.score[1] >= 2 and state['players'] == 1:
        enemy_paddle.speed = 10

    # Displays win or lose message accordingly
    if scoreboard.score[0] == 7:
        if state['players'] == "1":
            scoreboard.game_win()
        else:
            scoreboard.p_one_win()
        state['game_playing'] = False
    elif scoreboard.score[1] == 7:
        if state['players'] == "1":
            scoreboard.game_lose()
        else:
            scoreboard.p_two_win()
        state['game_playing'] = False

turtle.done()


