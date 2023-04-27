"""Tests for imshowtk"""

from tkinter import Tk
import cv2
from imshowtk.imshowtk import bitmap_to_photo, ImshowTk

def test_tk_is_working():
    """On some macos runners TK doesn't get set up properly
    We can quickly check for that here.
    """
    try:
        _ = Tk(None)
    except RuntimeError:
        #we're getting runtime errors on some macos CI.
        #https://github.com/actions/setup-python/issues/649
        assert False

def test_bitmap_to_photo():
    """bitmap_to_photo runs"""
    window = Tk(None)
    image = cv2.imread('project-icon.png')
    print (image.shape)

    _ = bitmap_to_photo(image)
    window.destroy()

def test_mmshowtk_not_in_use():
    """imshow does nothing if not in use"""
    imshow = ImshowTk(in_use = False)
    frame = cv2.imread('project-icon.png')
    imshow.imshow(frame)
    del imshow

def test_imshowtk_in_use():
    """imshow shows frame when in use"""
    imshow = ImshowTk()
    frame = cv2.imread('project-icon.png')
    imshow.imshow(frame)
    del imshow
