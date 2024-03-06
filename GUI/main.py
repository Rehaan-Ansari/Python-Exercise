from tkinter import *

class Student():    
    def __init__(self, name):
        self.first_name = name
        
    def set_grade(self, grade):
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
def show_grade():
    grade_label.config(text=csc_2[0].get_grade())
    pass

csc_2 = []

csc_2.append(Student("Tharoon"))
csc_2[0].set_grade("Not Achieved")

window =Tk()
window.geometry("500x500")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="show grade")
show_grade_btn.pack()

window.mainloop*()