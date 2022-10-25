from rpi_hardware_pwm import HardwarePWM
import time
from numpy import interp

# setup
servo_1 = HardwarePWM(pwm_channel=0, hz=50)
servo_1.start(6.5)

engines = HardwarePWM(pwm_channel=1, hz=60)
engines.start(0)

def set_steering(steering_val):
    duty = interp(steering_val, [-255, 255], [2.5, 10.5])
    servo_1.change_duty_cycle(duty)

def set_movement(acc_val, rev_val):
    if acc_val > 0 and rev_val == 0:
        speed =  acc_val
        pass # set forward pin
    if acc_val == 0 and rev_val >= 0:
        speed = rev_val
        pass # set backward pin
    else:
        speed = 0
    
    engines.change_duty_cycle(interp(steering, [0, 255], [0, 100]))

def set_input_params(input_params):
    set_steering(input_params['steering'])
    set_movement(input_params['acceleration'], input_params['reverse'])



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