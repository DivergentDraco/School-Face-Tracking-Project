"""
  Copyright (c) 2021 Eyeware Tech SA http://www.eyeware.tech

  This file provides an example on how to receive head and eye tracking data
  from Beam SDK.

  Dependencies:
  - Python 3.6
  - NumPy
"""

from eyeware.client import TrackerClient
import time
import numpy as np
import pyautogui

from pynput.mouse import Controller
from pynput import keyboard
from pynput.keyboard import Key

mouse = Controller()
Mode = False

def on_press(key):
    global Mode
    if key == Key.f10:
        if Mode:
            Mode = False
        else:
            Mode = True

listener = keyboard.Listener(on_press=on_press)
listener.start()

pyautogui.FAILSAFE = False

# Get screen width and height
screen_w, screen_h = pyautogui.size()

# Initialize tracker client
tracker = TrackerClient()

# Run forever, until we press ctrl+c
while True:
    # Ensure the tracker server connection is active
    if tracker.connected:
        print("  * Head Pose:")
        head_pose = tracker.get_head_pose_info()
        head_is_lost = head_pose.is_lost
        print("      - Lost track:       ", head_is_lost)
        if not head_is_lost:
            print("      - Session ID:       ", head_pose.track_session_uid)
            rot = head_pose.transform.rotation
            print("      - Rotation:          |%5.3f %5.3f %5.3f|" % (rot[0, 0], rot[0, 1], rot[0, 2]))
            print("                           |%5.3f %5.3f %5.3f|" % (rot[1, 0], rot[1, 1], rot[1, 2]))
            print("                           |%5.3f %5.3f %5.3f|" % (rot[2, 0], rot[2, 1], rot[2, 2]))
            tr = head_pose.transform.translation
            print("      - Translation:       <x=%5.3f m, y=%5.3f m, z=%5.3f m>" % (tr[0], tr[1], tr[2]))

        print("  * Gaze on Screen:")
        screen_gaze = tracker.get_screen_gaze_info()
        screen_gaze_is_lost = screen_gaze.is_lost
        print("      - Lost track:       ", screen_gaze_is_lost)
        if not screen_gaze_is_lost:
            print("      - Screen ID:        ", screen_gaze.screen_id)
            print("      - Coordinates:       <x=%5.3f px,   y=%5.3f px>" % (screen_gaze.x, screen_gaze.y))
            print("      - Confidence:       ", screen_gaze.confidence)

            # Move the mouse cursor to gaze coordinates
            gaze_x = screen_gaze.x
            gaze_y = screen_gaze.y
            pyautogui.moveTo(gaze_x, gaze_y)

        # Add a delay to match the tracker update rate (30 Hz)
        time.sleep(1 / 30)
    else:
        # Handle the case when the tracker is disconnected
        MESSAGE_PERIOD_IN_SECONDS = 2
        time.sleep(MESSAGE_PERIOD_IN_SECONDS - time.monotonic() % MESSAGE_PERIOD_IN_SECONDS)
        print("No connection with tracker server")