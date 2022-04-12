import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./Day025/usa_game/blank_states_img.gif"

data = pandas.read_csv("./Day025/usa_game/50_states.csv")

screen.addshape(image)

turtle.shape(image)

data_states = data["state"].to_list()

score = 0

while score < 50:
    answer = screen.textinput(title=f"{ score }/50 States Correct", prompt="What's another state's name ? ").title()

    if answer == "Exit":
        break

    if answer in data_states:

        data_states.remove(answer)
        score += 1
        data_state = data[data['state'] == answer]

        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data_state.x), int(data_state.y))
        t.write(data_state['state'].to_string(index=False))
        

pandas.DataFrame(data_states).to_csv("./Day025/usa_game/states_to_learn.csv")
