from tkinter import *

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {} 

    def get_grades(self):
        return self.grades

    def set_grade(self, subject, grade):
        self.grades[subject] = grade

def show_grades(event):
    selected_index = name_listbox.curselection()
    if selected_index:
        selected_student = csc_2[selected_index[0]]
        grades = selected_student.get_grades()
        grade_label.config(text=f"Grades for {selected_student.name}:\n{grades}")

csc_2 = []

student1 = Student("Amon")
student1.set_grade("CMS", "Achieved")

student2 = Student("Bilal")
student2.set_grade("CMS", "Merit")

student3 = Student("Tharin")
student3.set_grade("CMS", "Excellence")

csc_2.extend([student1, student2, student3])

window = Tk()
window.geometry("500x500")

name_listbox = Listbox(window)
for student in csc_2:
    name_listbox.insert(END, student.name)

name_listbox.pack()

grade_label = Label(window, justify=LEFT)
grade_label.pack()

name_listbox.bind("<Double-Button-1>", show_grades)

window.mainloop()
