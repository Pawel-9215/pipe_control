from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO 
import time
from numpy import interp
GPIO.setwarnings(False) 

# setup
servo_1 = HardwarePWM(pwm_channel=0, hz=50)
servo_1.start(6.5)

engines = HardwarePWM(pwm_channel=1, hz=60)
engines.start(0)

GPIO.setmode(GPIO.BCM) 

forward = 27
backward = 22

GPIO.setup(forward, GPIO.OUT)
GPIO.setup(backward, GPIO.OUT) 

def set_steering(steering_val):
    duty = interp(steering_val, [-255, 255], [3, 11])
    servo_1.change_duty_cycle(duty)

def set_movement(acc_val, rev_val):
    if acc_val > 2 and rev_val == 0:
        speed =  acc_val
        GPIO.output(backward, False)
        GPIO.output(forward, True)
        # set forward pin
    elif acc_val == 0 and rev_val > 2:
        speed = rev_val
        GPIO.output(forward, False)
        GPIO.output(backward, True)
        # set backward pin
    else:
        speed = 0
    
    engines.change_duty_cycle(interp(speed, [0, 255], [0, 100]))

def set_input_params(input_params):
    # print(input_params)
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