import cv2
from tkinter import Tk, Canvas, NW
from imshowtk.imshowtk import imshowTk, bitmap_to_photo

window = Tk()

capture = cv2.VideoCapture(0)
my_imshow = imshowTk(in_use = True)

for frame_number in range (200):
    _, frame = capture.read()

    my_imshow.imshow(frame)

capture.release()

image = cv2.imread('project-icon.png')
print (image.shape)
canvas = Canvas(window,
                width = image.shape[1], height = image.shape[0])
canvas.pack()

photoImage = bitmap_to_photo(image)
canvas.create_image(0, 0, anchor=NW, image=photoImage)

window.mainloop()

