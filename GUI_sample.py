from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("ANSA")
window.configure(bg="#900C3F")


def Hello():
    print("button clicked")


#button = Button(window, text="ok", command=Hello, width=30, height=10, fg="red")
button = Button(window, text="ok", command=Hello)
label = Label(window, text="welcome,\n hai")

button.pack()
label.pack()

window.mainloop()
print("hai")
