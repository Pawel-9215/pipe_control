This is code for my raspberryPi wifi controlled car with webcam feed, ale done in python.

control_node.py <- that's the server that needs to be run first on the computer
raspi_client.py <- this is cliend you can run remotely via ssh on raspberry.

Connection is established by python socket library.

Gamepad:
right trigger - acceleration
left trigger - reverse

left thumbstick - steering left and right

space - change gamepad mapping between windows and linux

you need rpi_hardware_pwm library on raspberry
and pygame on server pc
