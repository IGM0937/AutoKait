import tkinter as tk


is_selected = False


def on_click(value=None):
    global is_selected

    if value is None:
        value = is_selected

    if value:
        # change image on canvas
        canvas.itemconfig(image_id, image=unselected_img)
    else:
        canvas.itemconfig(image_id, image=selected_img)

    is_selected = not value


# Taken from https://blog.furas.pl/python-tkinter-update-image-on-canvas-with-button-click-gb.html
if __name__ == '__main__':
    root = tk.Tk()

    # create images
    unselected_img = tk.PhotoImage(file="../img/ball1.gif")
    selected_img = tk.PhotoImage(file="../img/ball2.gif")

    # canvas for image
    canvas = tk.Canvas(root, width=60, height=60)

    # set first image on canvas
    image_id = canvas.create_image(0, 0, anchor='nw', image=unselected_img)
    # Events list https://www.python-course.eu/tkinter_events_binds.php
    canvas.tag_bind(image_id, '<Button-1>', lambda e: on_click())

    # pack canvas onto window
    canvas.pack()

    # button to change image
    button1 = tk.Button(root, text="Force Green", command=lambda: on_click(False))
    button1.pack()
    button2 = tk.Button(root, text="Force Red", command=lambda: on_click(True))
    button2.pack()

    root.mainloop()
