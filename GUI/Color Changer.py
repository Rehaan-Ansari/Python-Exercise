import tkinter as tk

def change_color(color):
    main_window['bg'] = color

main_window = tk.Tk()
main_window.title("Color Changer")

for color in ["red", "blue"]:
    button = tk.Button(main_window, text=color.capitalize(), command=lambda c=color: change_color(c))
    button.pack(pady=10)

main_window.mainloop()