from tkinter import Label, Tk 
import time
app_window = Tk() 
app_window.title("First Project") 
app_window.geometry("300x250") 

text_font= ("Times", 40, 'bold')
background = "black"
foreground= "white"
border_width = 12

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
# label.grid(row=0, column=1)
label.pack()
label.config(text="hello")

app_window.mainloop()