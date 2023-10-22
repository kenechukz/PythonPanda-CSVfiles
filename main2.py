import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
pen = turtle.Turtle()
pen.hideturtle()
turtle.shape(image)
states = pandas.read_csv('50_states.csv')
states_list = states.state.to_list()
#xcord_list = states.x.to_list()
#ycord_list = states.y.to_list()
states = states.to_dict()
print(states)
#coords_list = [states.x,states.y]
#print(xcord_list)
print(states_list)

count = 0

guesses = []

state_index = 0

while count != 50:

    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another states name?")
    #print(answer_state)

    for state in states_list:
        if answer_state.lower() == state.lower():
            count+= 1
            state_index = states_list.index(state)
            #print(state_index)
            state_xcor = states['x'][state_index]
            state_ycor = states['y'][state_index]
            pen.pu()
            pen.setpos(state_xcor, state_ycor)
            pen.pd()
            pen.write(state,font=('Arial', 12, 'normal'))
            #print(state_xcor,state_ycor)
    
    guesses.append(answer_state)
        

    


screen.exitonclick()
