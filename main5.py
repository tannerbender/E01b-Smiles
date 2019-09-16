#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smiley Face Example"

class Faces(arcade.Window): # create a class that extends the arcade.Window class
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2 # This is the starting x position 
        self.y = SCREEN_HEIGHT / 2 #This is the starting y position

        arcade.set_background_color(open_color.white) # Sets the background color to white

    def on_draw(self):
        """ Draw the face """
        arcade.start_render() # begin the process of rendering this face
        face_x,face_y = (self.x,self.y) # simply get the points
        smile_x,smile_y = (face_x + 0,face_y - 10) # This adjusts where the smile is in relation to the center
        eye1_x,eye1_y = (face_x - 30,face_y + 20) # adjusts where eye is
        eye2_x,eye2_y = (face_x + 30,face_y + 20) # adjusts where eye is
        catch1_x,catch1_y = (face_x - 25,face_y + 25) # adjusts where center of eye is
        catch2_x,catch2_y = (face_x + 35,face_y + 25) # adjusts where center of eye is

        #lines 38-44 draw all of the face components like earlier
        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)


    def on_mouse_motion(self, x, y, dx, dy):# every time the mouse moves call this function
        """ Handle Mouse Motion """
        self.x = x # setting the x position of the face to the x position of the mouse
        self.y = y # setting the y position of the face to the x position of the mouse



window = Faces()
arcade.run()