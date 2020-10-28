from VirtualCopernicusNG import TkCircuit
from common_code.common_cx_code import is_for_me, do_my_job
from common_code.udp_receiver import  udp_reciver_check_messages, udp_reciver_init
from common_code.udp_controller import udp_controller

# initialize the circuit inside the

configuration = {
    "name": "c2",
    "sheet": "sheet_smarthouse.png",
    "width": 332,
    "height": 300,
    "leds": [
        {"x": 112, "y": 70, "name": "LED 1", "pin": 21},
        {"x": 71, "y": 141, "name": "LED 2", "pin": 22}
    ],
    "buttons": [
        {"x": 242, "y": 146, "name": "Button 1", "pin": 11},
        {"x": 200, "y": 217, "name": "Button 2", "pin": 12},
    ],
    "buzzers": [
        {"x": 277, "y": 9, "name": "Buzzer", "pin": 16, "frequency": 440},
    ]
}

circuit = TkCircuit(configuration)
who_i_am = ['f0', 'kitchen', 'c2'] # floor, bedroom, device


@circuit.run
def main():
    # now just write the code you would use on a real Raspberry Pi

    from gpiozero import LED, Button
    from time import sleep

    from gpiozero import Buzzer
    buzzer = Buzzer(16)

    led1 = LED(21) # id 1
    devices = [led1]

    def button1_pressed():
        print("button 1 pressed!")
        led1.toggle()

    def button2_pressed():
        print("button 1 pressed!")
        udp_controller("f0;living_room;c1;1;change")

    
    button1 = Button(11)
    button1.when_pressed = button1_pressed

    button2 = Button(12)
    button2.when_pressed = button2_pressed

    sock = udp_reciver_init()

    while True:
        command = udp_reciver_check_messages(sock)
        print(command)
        if(is_for_me(command, who_i_am)):
            do_my_job(command[3], command[4], devices)
        sleep(0.1)