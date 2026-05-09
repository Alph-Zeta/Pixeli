import tkinter as tk


root = tk.Tk()
root.geometry("1000x900")
root.config(bg = "black")     
label = tk.Label(root , text = "LOGO" ,
                 font = ("my_fixed",170) ,
                 bd = 5,
                 bg = "black",
                 fg = "#FF6B00")

label.pack(
           anchor = "w",
           padx = 90 ,
           pady = 10)

label_1 = tk.Label(root, text = "MACHINERIUS",
                   font = ("mine-sweeper" , 50),  
                   bg = "black",
                   fg = "#00FF00"
                    
                   )

label_1.pack(side = "left" , pady = 50 , padx = 100)

root.mainloop()

