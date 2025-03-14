import turtle
import pandas as pd

#add the US map 
screen = turtle.Screen()
screen.title("U.S. State Game")

#load the map as a new shape
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states= data.state.to_list()
guessed_state =[]

while len(guessed_state) < 50:

#Pop up box
#keep track of score
# Using title(), when the input name is lower case or camel case.
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct", prompt="What's another state's name?").title()

    #Convert the guess to Title case
    if answer_state in all_states:

        #Add answer_state to the guessed_state
        guessed_state.append(answer_state)
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



