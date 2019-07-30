import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    snake_stamp = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(snake_stamp)
for i in range (START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()
    def remove_tail():
        old_stamp = stamp_list.pop(0) # last piece of tail
        snake.clearstamp(old_stamp) # erase last piece of tail
        pos_list.pop(0) # remove last piece of tail's position
snake.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def Up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")
def Down():
    snake.direction="Down" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")
def Left():
    snake.direction="Left" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")
def Right():
    snake.direction="Rigt" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")
#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!
 # Create listener for up key
turtle.onkeypress(Up, "Up")
turtle.onkeypress(Down, "Down")
turtle.onkeypress(Left, "Left")
turtle.onkeypress(Right, "Right")
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #Add this line to the end of the move_snake function
    turtle.ontimer(move_snake,TIME_STEP) #<--- new line here

#Now, call the move_snake() function.  This starts moving the snake.  Once it starts 
#moving, it keeps moving by itself:

    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    turtle.ontimer(move_snake,TIME_STEP)
    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    elif new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()
     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE

    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif snake.direction=="Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif snake.direction=="Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()
     #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    
    #HINT: This if statement may be useful for Part 8

    ...
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()
    
move_snake()

turtle.listen()
#ADD THE LINES BELOW

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:

#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
for this_food_pos in food_pos :
    ####WRITE YOUR CODE HERE!!
    food.goto(this_food_pos)
    food.stamp()
    food_stamps.append(food.pos())
turtle.mainloop()
