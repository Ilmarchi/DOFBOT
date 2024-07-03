#Qui vengono importati tutti i vari moduli che fanno funzionare il programma

import enum

import cv2

import time

import numpy as np

from Arm_Lib import Arm_Device


def get_color(img):

     H = []
     S = []
     V = []
     color_name={}

     img = cv2.resize(img, (640, 480))

     # Convert color image to HSV

     HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

     # Draw a rectangular frame

     cv2.rectangle(img, (280, 180), (360, 260), (0, 255, 0), 2)

     # Take out the H, S, and V values of each row and column in turn and put them into the container.

     for i in range(280, 360):

         for j in range(180, 260): 
             H.append(HSV[j, i][0])
             S.append(HSV[j, i][1])
             V.append(HSV[j, i][2])
     # Calculate the maximum and minimum values of H, S, and V respectively
     
     H_min = min(H);H_max = max(H)
     S_min = min(S);S_max = max(S)
     V_min = min(V);V_max = max(V)

     # Determine color

     if (( H_min >= 0 and H_max <= 10 ) or ( H_min >= 0 and H_max <= 180 ) ) and ( S_min >= 155 and S_min <= 230 ) and ( V_min >= 160 and V_max <= 220 )  : color_name['name'] = 'red'

     elif H_min >= 20 and H_max <= 30: color_name['name'] = 'yellow'

     elif H_min >= 31 and H_max <= 60: color_name['name'] = 'green'

     elif H_min >= 100 and H_max <= 112: color_name['name'] = 'blue'

     return img, color_name
     
#Initializing the Arm and the VideoCapture (for the pictures)     
     
Arm = Arm_Device()

cap = cv2.VideoCapture(0)

cap.set(3, 640)

cap.set(4, 480)

cap.set(5, 30) #Set frame rate

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))


# Red is selected by default, and the program will automatically switch colors based on the color detected in the box.

# red interval

color_lower = np.array([0, 43, 46])

color_upper = np.array([10, 255, 255])



# Principal function where i take a picture and pass it to a function that returns the color

def Color_Recongnize():

    
    Arm.Arm_serial_servo_write6(s1=97, s2=75, s3=22, s4=3, s5=90, s6=90,time=1000 )
    time.sleep(1)
    flag = 0
    global cap
    while(1):
        # get a frame and show Get the video frame and convert it to HSV format. Use cvtColor() to convert the BGR format to HSV format. The parameter is cv2.COLOR_BGR2HSV.
        flag = 0
        ret, frame = cap.read()
        if not ret:
            continue
        frame, color_name = get_color(frame)
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if len(color_name)==1:
            global color_lower

            global color_upper
            # I control the color_name and based on the id i move the arm in the direction
            if color_name['name'] == 'yellow':
                print( "yellow")
                flag = 1
                color_lower = np.array([26, 43, 46])
                color_upper = np.array([34, 255, 255])
            elif color_name['name'] == 'red':
                print( "red")
                flag = 2
                color_lower = np.array([0, 43, 46])
                color_upper = np.array([10, 255, 255])
            elif color_name['name'] == 'green':
                print( "green")
                flag = 3
                color_lower = np.array([35, 43, 46])
                color_upper = np.array([77, 255, 255])
            elif color_name['name'] == 'blue':
                print( "blue")
                flag = 4
                color_lower=np.array([100, 43, 46])
                color_upper = np.array([124, 255, 255])
        
        if not flag == 0 :
            moveArm( flag )
        time.sleep(0.01)
    cap.release()
        

# Function to move the arm in the right direction of the ID

def moveArm( flag ) :
    global cap
    cap.release()
    Arm.Arm_serial_servo_write6(s1=95, s2=60, s3=10, s4=45, s5=90, s6=75,time=1000 )
    time.sleep( 2 )
    Arm.Arm_serial_servo_write( 6 , 137,time=1000 )
    time.sleep( 2 )
    if flag == 4 :
        Arm.Arm_serial_servo_write(6,145,100)
        time.sleep(0.250)
        Arm.Arm_serial_servo_write6(s1=48, s2=70, s3=40, s4=20, s5=85, s6=145,time=1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=48, s2=55, s3=33, s4=11, s5=86, s6=145,time=1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write(6,90,500)
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=48, s2=70, s3=40, s4=20, s5=80, s6=145,time=1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=97, s2=75, s3=22, s4=3, s5=91, s6=150,time=2000 )
        time.sleep( 2 )

    if flag == 3 :
        Arm.Arm_serial_servo_write(6,145,100)
        time.sleep(0.250)
        Arm.Arm_serial_servo_write6(s1=140, s2=70, s3=40, s4=20, s5=105, s6=145,time=1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=140, s2=55, s3=35, s4=9, s5=95, s6=145,time=1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write(6,90,500)
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=140, s2=70, s3=40, s4=20, s5=105, s6=145,time=1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=97, s2=75, s3=22, s4=3, s5=90, s6=150,time=2000 )
        time.sleep( 2 )
      
    if flag == 1 :
        Arm.Arm_serial_servo_write(6,145,100)
        time.sleep(0.250)
        Arm.Arm_serial_servo_write6(s1=68, s2=30, s3=75, s4=50, s5=100, s6=145,time= 2000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=69, s2=18, s3=75, s4=40, s5=100, s6=150,time= 1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write(6,90,500)
        time.sleep(1)
        Arm.Arm_serial_servo_write6(s1=68, s2=30, s3=75, s4=50, s5=100, s6=145,time= 2000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=97, s2=75, s3=22, s4=3, s5=90, s6=150,time=2000 )
        time.sleep( 2 )
    if flag == 2 :
        Arm.Arm_serial_servo_write(6,145,100)
        time.sleep(0.250)
        Arm.Arm_serial_servo_write6(s1=125, s2=30, s3=75, s4=47, s5=80, s6=145,time= 2000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=120, s2=18, s3=75, s4=37, s5=80, s6=150,time= 1000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write(6,90,500)
        time.sleep(1)
        Arm.Arm_serial_servo_write6(s1=125, s2=30, s3=75, s4=75, s5=80, s6=145,time= 2000 )
        time.sleep(2)
        Arm.Arm_serial_servo_write6(s1=97, s2=75, s3=22, s4=3, s5=90, s6=150,time=2000 )
        time.sleep( 2 )

    # I reinitialize the VideoCapture for the new image

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(5, 30)  # Set frame rate
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))

try:
    Color_Recongnize()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass
