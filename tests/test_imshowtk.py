"""Tests for imshowtk"""

from tkinter import Tk
import cv2
from imshowtk.imshowtk import bitmap_to_photo

def test_bitmap_to_photo():
    """bitmap_to_photo runs"""
    try:
        window = Tk(None)
    except RuntimeError:
        #we're getting runtime errors on some macos CI.
        #https://github.com/actions/setup-python/issues/649
        #assert False
        return
    image = cv2.imread('project-icon.png')
    print (image.shape)

    _ = bitmap_to_photo(image)
    window.destroy()
