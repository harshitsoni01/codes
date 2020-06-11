from tkinter import *
m = Tk()#initializing the tkinter window
m.title("Title of GUI")
m.geometry("600x600")#size of the window # its "x" not "*"
thelabel = Label(m, text = "Welcome to GUI!")
thelabel.pack(side = TOP)#pack method for placements of objects
b1 = Button(m, text = "Button1", fg="white", bg="black")
b1.pack(side=LEFT)# (side = top, bottom, )
b2 = Button(m, text = "button2", font="comicsans, 14", width=15, height=2)
b2.pack(side=RIGHT)
#b3 = Button(m, text = "Button3")
#b3.grid(row = 1, column = 0)# grid method for placement of objects 
# you cannot mix grid and pack method
#the values of row=1,col=0 depend of the position of the other widget in your window
def close_window():
    m.destroy()
b4 = Button(m, text= "Exit",command = close_window)
b4.place(relx=0.5, rely=0.5, anchor=CENTER)
#this is udes to get image in tkinter
#img = ImageTk.PhotoImage(Image.open("True1.gif"))
#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
m.mainloop() 