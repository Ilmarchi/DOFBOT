import cv2
import time
from Arm_Lib import Arm_Device

Arm = Arm_Device()
time.sleep(.1)
image = cv2.VideoCapture(1)

width=648
height=480

def main():
    Arm.Arm_serial_servo_write6(s1=90, s2=90, s3=0, s4=90, s5=90, s6=90,time=2000 )
    time.sleep( 1)
    while True:
        rval, frame = image.read()
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    cv2.imwrite("./IMG/img.png", frame)
    image.release() 


try:
    main()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass