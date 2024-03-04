from tkinter import *
names = [] #need an empty list, that we will add names to it, so we can keep track of players and use them later for score board

class QuizStarter:
    def __init__(self, parent):#constructor, The init function is called automatically every time the class is being used to create a new object.
        
        background_color="OldLace"#to set it as a background color for all the label widget
        
        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#this geometry manager organizes widgets in a table-like structure in the parent widget.
        
        #label widget for the heading
        self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font=("TwCen Mt","18", "bold"), bg=background_color)
        self.heading_label.grid(row=0, padx=20)