import turtle
import pandas


states = pandas.read_csv("50_states.csv")
states_dict = states.to_dict()
states_name = states_dict["state"]
states_name_list = []

for i in range(len(states_name)):
    states_name_list.append(states_name[i])

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


t = turtle.Turtle()
t.penup()
t.hideturtle()

game_is_on = True
guessed_countries = []
score = 0

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 guessed states",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_name_list and answer_state not in guessed_countries:
        state = states[states["state"] == answer_state]
        coordinate = (int(state.x), int(state.y))
        score += 1
        guessed_countries.append(answer_state)
        t.goto(coordinate)
        t.write(arg=answer_state)

        if score >= 50:
            game_is_on = False

states_to_learn = [state for state in states_name_list if state not in guessed_countries]
states_df = pandas.DataFrame(states_to_learn)
print(states_df)
states_df.to_csv("states_to_learn.csv")
