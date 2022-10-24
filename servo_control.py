from rpi_hardware_pwm import HardwarePWM
import time
from numpy import interp

# setup
servo_1 = HardwarePWM(pwm_channel=0, hz=50)
servo_1.start(6.5)

def set_steering(steering_val):
    duty = interp(steering_val, [-255, 255], [2.5, 10.5])
    servo_1.change_duty_cycle(duty)

def set_acceleration(acc_val):
    pass

def set_reverse(rev_val):
    pass

def set_input_params(input_params):
    set_steering(input_params['steering'])
    set_acceleration(input_params['acceleration'])
    set_reverse(input_params['reverse'])


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