import tkinter as tk
import math


WIDTH = 60
HEIGHT = 60
RADIUS_BOUND = WIDTH/2
is_selected = False
mouse_x = None
mouse_y = None


def mouse_update(event):
    global mouse_x
    global mouse_y

    mouse_x = event.x
    mouse_y = event.y


def on_click(value=None):
    if not inbound():
        return

    global is_selected

    if value is None:
        value = is_selected

    canvas.itemconfig(image_id, image=(unselected_img if value else selected_img))
    is_selected = not value


def inbound():
    global mouse_x
    global mouse_y
    pos = canvas.coords(image_id)
    centre_x = pos[0]
    centre_y = pos[1]

    x = centre_x - mouse_x
    y = centre_y - mouse_y
    dis = math.sqrt((x ** 2) + (y ** 2))

    return dis < RADIUS_BOUND


if __name__ == '__main__':
    root = tk.Tk()

    # create images
    unselected_img = tk.PhotoImage(file="../img/ball1.gif")
    selected_img = tk.PhotoImage(file="../img/ball2.gif")

    # canvas for image
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    # set first image on canvas
    image_id = canvas.create_image(WIDTH/2, HEIGHT/2, image=unselected_img)
    canvas.tag_bind(image_id, '<Button-1>', lambda e: on_click())
    canvas.bind('<Enter>', mouse_update)
    canvas.bind('<Motion>', mouse_update)
    # pack canvas onto window
    canvas.pack()

    root.mainloop()
