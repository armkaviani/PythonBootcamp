import turtle

#add the US map 
screen = turtle.Screen()
screen.title("U.S. State Game")

#load the map as a new shape
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


#For fetching the coordinate the states
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

#alternative way of keeping the screen open 
turtle.mainloop()

