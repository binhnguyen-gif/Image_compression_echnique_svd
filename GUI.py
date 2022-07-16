import timeit
import tkinter as tk
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk
from sklearn.feature_extraction import image

from Image import *

root = tk.Tk()
root.title("SVD Image Compressor")

canvas = tk.Canvas(root, height=0, width=100)
canvas.pack()

frame = tk.Frame(root, bg='#262626')
frame.place(relwidth=0, relheight=0)


def save(filenew):
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    filenew.save(filename)


def file():
    global my_image
    global my_label
    global my_image_label
    global filename
    root.filename = filedialog.askopenfilename(
        initialdir="C:/Users/Wind/Downloads/Images", title="Select a file", filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("png files", "*.png")))
    my_label = Label(root, text=root.filename).pack()
    button1.forget()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
    # my_image_label.place(x=10, y=10)


def compress():

    img = openImage(root.filename)
    start = timeit.default_timer()
    imageWidth = 512
    imageHeight = 512

    # số lượng giá trị đơn lẻ được sử dụng để tạo lại hình ảnh đã nén
    singularValuesLimit = 160

    aRedCompressed = compressSingleChannel(img[0], singularValuesLimit)
    aGreenCompressed = compressSingleChannel(img[1], singularValuesLimit)
    aBlueCompressed = compressSingleChannel(img[2], singularValuesLimit)

    imr = Image.fromarray(aRedCompressed, mode=None)
    img = Image.fromarray(aGreenCompressed, mode=None)
    imb = Image.fromarray(aBlueCompressed, mode=None)

    newImage = Image.merge("RGB", (imr, img, imb))
    # root.withdraw()
    # imagenew = tk.Tk()
    root.title("Ảnh sau nén")
    anh = ImageTk.PhotoImage(image=newImage)
    canvas = tk.Canvas(root, width=200, height=270)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=anh)
    button2 = tk.Button(root, text="Save", bg='green', fg="red",
                        font='Helvetica', command=lambda: save(newImage))
    button2.pack(side='bottom', fill='both')
    mr = imageHeight
    mc = imageWidth
    originalSize = mr * mc * 3
    compressedSize = singularValuesLimit * (1 + mr + mc) * 3
    stop = timeit.default_timer()
    print('Kích thước ban đầu: %d' % originalSize)
    print('Kích thước nén: %d' % compressedSize)
    print('Tỉ lệ kích thước nén / kích thước ban đầu:')
    ratio = compressedSize * 1.0 / originalSize
    print(ratio)
    print('Kích thước hình ảnh được nén ' +
          str(round(ratio * 100, 2)) + '% hình ảnh gốc ')
    print('Time: ', stop - start)
    root.mainloop()


button1 = tk.Button(root, bg='#262626', fg='black', command=file)
button1.pack(side='top', fill='both')
plusimage = PhotoImage(file="Snapshots/mainscreen.png")
button1.config(image=plusimage)
size = plusimage.subsample(2, 2)
button1.config(image=size)

button = tk.Button(root, text="compress image", bg='green',
                   font='Helvetica', command=compress)
button.pack(side='bottom', fill='both')
root.mainloop()
