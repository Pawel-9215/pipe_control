from rpi_hardware_pwm import HardwarePWM
import time
from numpy import interp

# setup
servo_1 = HardwarePWM(pwm_channel=0, hz=50)


if __name__ == '__main__':
    servo_1.start(100)
    quiter = 998

    while quiter != 999.0:
        steering = float(input())
        quiter = steering
        duty = interp(steering, [-255, 255], [2.5, 10.5])
        servo_1.change_duty_cycle(duty)
    
    servo_1.stop()
    #Clean things up at the end
    print ("Goodbye")