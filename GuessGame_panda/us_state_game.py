import turtle
import pandas as pd

#add the US map 
screen = turtle.Screen()
screen.title("U.S. State Game")

#load the map as a new shape
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

#Pop up box
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

data = pd.read_csv("50_states.csv")
all_states= data.state.to_list()

#Convert the guess to Title case
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    #with item(), accessing the single item contained in panda. Because with state_data.x, it tries to access the index and column.
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(answer_state)


screen.exitonclick()






#For fetching the coordinate the states
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

#alternative way of keeping the screen open 
#turtle.mainloop()



