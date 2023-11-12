
#importing the Tkinter and color chooser modules
import tkinter as tk
from tkinter.colorchooser import askcolor


# function to start drawing
def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing =True
    prev_x, prev_y = event.x, event.y


#function to actually draw on the whiteboard
def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(current_x, current_y,prev_x, prev_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y =current_x, current_y


#function to stop drawing
def stop_drawing(event):
    global is_drawing
    is_drawing = False


#implementing the color-changing function
def change_pen_color():
    global drawing_color
    color= askcolor()[1]
    if color:
        drawing_color = color


#function to adjust the line width
def change_line_width(value):
    global line_width
    line_width = int(value)

#creating a window with a title and a white canvas
root=tk.Tk()
root.title("Whiteboard app")

canvas=tk.Canvas(root,bg="white")
canvas.pack(fill="both",expand=True)

is_drawing=False
drawing_color="black"
line_width=2
root.geometry("700x600")


# create a frame to hold the buttons or controls in the same line
controls_frame=tk.Frame(root)
controls_frame.pack(side="top",fill="x")

color_button= tk.Button(controls_frame, text="Change Color",command=change_pen_color)
clear_button= tk.Button(controls_frame, text="Clear",command=lambda: canvas.delete("all"))

color_button.pack(side="left",padx=5,pady=5)
clear_button.pack(side="left",padx=5,pady=5)


# a slider for the line width function
line_width_label=tk.Label(controls_frame,text="Line Width:")
line_width_label.pack(side="left",padx=5,pady=5)

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))
line_width_slider.set(line_width)
line_width_slider.pack(side="left",padx=5,pady=5)

canvas.bind("<Button-1>",start_drawing)
canvas.bind("<B1-Motion>",draw)
canvas.bind("<ButtonRelease-1>",stop_drawing)

root.mainloop()