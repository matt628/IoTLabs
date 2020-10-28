from VirtualCopernicusNG import TkCircuit

from common_code.udp_controller import udp_controller
# initialize the circuit inside the

configuration = {
    "name": "c4",
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

@circuit.run
def main():
    # now just write the code you would use on a real Raspberry Pi

    from gpiozero import LED, Button
    from time import sleep

    led1 = LED(21)
    led2 = LED(22)

    def button1_pressed():
        print("button 1 pressed!")
        led1.toggle()
        

    def button2_pressed():
        led1.off()
        print("button 2 pressed - all lights will be switched off")
        udp_controller("f0;*;*;*;off")
    
    button1 = Button(11)
    button1.when_pressed = button1_pressed

    button2 = Button(12)
    button2.when_pressed = button2_pressed


    while True:
        sleep(0.1)