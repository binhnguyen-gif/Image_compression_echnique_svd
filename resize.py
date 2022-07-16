
from tkinter import *
from PIL import Image, ImageTk


root = Tk()

image = Image.open("anhsau.png")

resize_image = image.resize((250, 250))

img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img)
label1.image = img
label1.pack()

# Execute Tkinter
root.mainloop()


# from PIL import Image

# im = Image.open(r"anhsau.png")

# width, height = im.size
# left = 5
# top = height / 4
# right = 164
# bottom = 3 * height / 4

# im1 = im.crop((left, top, right, bottom))
# im1.show()
