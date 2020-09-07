from tkinter import *


root = Tk()
root.title("Hello")
root.geometry("500x500")


canvas = Canvas(root, width = 400, height = 400, bg="white")
canvas.pack(pady=20)


# canvas.create_line(0 , 100, 300, 100, fill="red")



glow = canvas.winfo_pointerx()
canvas.dra

root.mainloop()