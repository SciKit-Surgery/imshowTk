"""Tests for imshowtk"""

from tkinter import Tk
import cv2
from imshowtk.imshowtk import bitmap_to_photo

def test_bitmap_to_photo():
    """bitmap_to_photo runs"""
    window = Tk(None)
    image = cv2.imread('project-icon.png')
    print (image.shape)

    _ = bitmap_to_photo(image)
    window.destroy()
