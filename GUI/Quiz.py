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
        self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font=("Times New Roman","18", "bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20)
        
        #holds value of radio buttons
        self.var1=IntVar()
        
        #label for username
        self.user_label=Label (self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT", "16"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)

        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        
        #continue button
        self.continue_button= Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection) 
        self.continue_button.grid(row=3, padx=20, pady=20)
        
    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning 
        self.quiz_frame.destroy() #destroy the starter window
        

if __name__ =="__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quiz_instance= QuizStarter (root) #instantiation, making an instance of the class QuizStarter 
    root.mainloop() #so the window doesnt dissapear