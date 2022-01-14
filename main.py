import turtle
import pandas as p

# create screen
screen = turtle.Screen()
# gives title to our screen
screen.title("U.S. State Quiz Game")
# defining image we want on the screen
image = "blank_states_img.gif"
screen.addshape(image)
# adds image to the screen
turtle.shape(image)

# reads the csv file
state_data = p.read_csv("50_states.csv")

# an empty list
guessed_state = []

# runs the program until all the states are not counted
while len(guessed_state) < 50:
    # takes the input of the user's guessed state
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="Enter another state's name or "
                                                                                      "'q' to Quit : ").title()
    # converts all the states from "state_data" to a list
    all_states = state_data.state.to_list()

    # exits the game
    if answer == 'Q':
        remaining_states = [state for state in all_states if state not in guessed_state]
        # creates the list of states which user was unable to guess
        new_states = p.DataFrame(remaining_states)
        new_states.to_csv("learn_states.csv")
        break

    # Executes, when user's input is in the all_states
    if answer in all_states:
        # correct answer gets stored in the "guessed_states"
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # provides the particular state information
        state_info = state_data[state_data.state == answer]
        # takes the state to the right position
        t.goto(float(state_info.x), float(state_info.y))
        # prints the answered state on the provided coordinates
        t.write(f"{answer}")
