import time
from Arm_Lib import Arm_Device

def main():
    Arm = Arm_Device()
    Arm.Arm_serial_servo_write6(s1=90, s2=110, s3=10, s4=10, s5=90, s6=90,time=1000 )

try:
    main()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass