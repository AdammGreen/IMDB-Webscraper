from tkinter import *


root = Tk()

#define image
bg = PhotoImage(file = "movieAppGUI.png")


#create a label
my_label= Label(root, image= bg)
my_label.place(x=0,y=0, relwidth=1,relheight=1)


#gives button functionality
def myClick():
   

#display the button with text on it
    myButton = Button(root, text="I hope you understand! Click me to confirm understanding", padx=50, pady=50,command=myClick)
    myButton.pack()

    myLabel = Label(root, text = "Great! Now go search and get the popcorn ready!")
    myLabel.pack()

root.mainloop()




