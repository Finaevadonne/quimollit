   from tkinter import *
   
   root = Tk()
   frame = Frame(root)
   frame.pack()  # Pack the frame into the root window
   
   button = Button(frame, text="Click me")
   button.pack(side=LEFT)  # Pack the button into the frame, on the left side
   
   root.mainloop()
   