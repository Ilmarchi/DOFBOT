import enum

import cv2

def bgr8_to_jpeg(value, quality=75):

     return bytes(cv2.imencode('.jpg', value)[1])

import traitlets

import ipywidgets.widgets as widgets

import time

# Thread function operation library

import threading

import inspect

import ctypes


origin_widget = widgets.Image(format='jpeg', width=320, height=240)

mask_widget = widgets.Image(format='jpeg',width=320, height=240)

result_widget = widgets.Image(format='jpeg',width=320, height=240)


# Create a horizontal box container to place image widgets next to each other

image_container = widgets.HBox([origin_widget, mask_widget, result_widget])

# image_container = widgets.Image(format='jpeg', width=600, height=500)



def get_color(img):

    H = []

    color_name={}

    img = cv2.resize(img, (640, 480), )

    # Convert color image to HSV

    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Draw a rectangular frame

    cv2.rectangle(img, (280, 180), (360, 260), (0, 255, 0), 2)


    cv2.imshow('rect', img)
    cv2.waitKey(10)

     # Take out the H, S, and V values of each row and column in turn and put them into the container.

    for i in range(280, 360):

        for j in range(180, 260): H.append(HSV[j, i][0])

     # Calculate the maximum and minimum values of H, S, and V respectively

    H_min = min(H);H_max = max(H)

# print(H_min,H_max)

     # Determine color

    if H_min >= 0 and H_max <= 10 or H_min >= 156 and H_max <= 180: color_name['name'] = 'red'

    elif H_min >= 20 and H_max <= 30: color_name['name'] = 'yellow'

    elif H_min >= 31 and H_max <= 60: color_name['name'] = 'green'

    elif H_min >= 100 and H_max <= 112: color_name['name'] = 'blue'

    print(color_name)
    return H_min, H_max


import cv2

import numpy as np

import ipywidgets.widgets as widgets

import time
from Arm_Lib import Arm_Device

Arm = Arm_Device()

cap = cv2.VideoCapture(1)

cap.set(3, 640)

cap.set(4, 480)

cap.set(5, 30) #Set frame rate

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))


# Red is selected by default, and the program will automatically switch colors based on the color detected in the box.

# red interval

color_lower = np.array([0, 43, 46])

color_upper = np.array([10, 255, 255])



def Color_Recongnize():

    
    Arm.Arm_serial_servo_write6(s1=90, s2=90, s3=10, s4=0, s5=90, s6=90,time=1000 )
    time.sleep(1)
    flag = 0
    
    while(1):
        if flag == 0 :
            # get a frame and show Get the video frame and convert it to HSV format. Use cvtColor() to convert the BGR format to HSV format. The parameter is cv2.COLOR_BGR2HSV.

            ret, frame = cap.read()

            val1, val2 = get_color(frame)

            print( val1 , val2 )
            time.sleep(0.01)

    cap.release()

     #cv2.destroyAllWindows()
    


try:
    Color_Recongnize()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass