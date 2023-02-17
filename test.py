# make turtle game by python

import turtle

# Create a window
window = turtle.Screen()
window.title("Turtle Game")
window.bgcolor("lightgreen")
window.setup(width=600, height=600)

# Create a turtle 
turtle1 = turtle.Turtle() 
turtle1.shape("turtle") 
turtle1.color("blue") 
turtle1.speed(2) 

 # Draw the square 
for i in range(4): 

    # Move the turtle forward by 100 units 
    turtle1.forward(100)

    # Turn the turtle by 90 degree  
    turtle1.right(90)  

 # Draw the circle  
turtle1.circle(50)  

 # Keep the window open until user closes it  
window.mainloop()