from VirtualCopernicusNG import TkCircuit

# initialize the circuit inside the

configuration = {
    "name": "CopernicusNG Weather Forecast",
    "sheet": "sheet_forecast.png",
    "width": 400,
    "height": 267,

    "servos": [
        {"x": 170, "y": 150, "length": 90, "name": "Servo 1", "pin": 17}
    ],
    "buttons": [
    {"x": 295, "y": 200, "name": "Button 1", "pin": 11},
    {"x": 295, "y": 170, "name": "Button 2", "pin": 12},
    ], 
    "leds": [
        {"x": 380, "y": 70, "name": "LED 1", "pin": 21},
        {"x": 380, "y": 141, "name": "LED 2", "pin": 22}
    ],
}

circuit = TkCircuit(configuration)


def status_to_angle(status):
    status_to_angle = {
        'Clear': -75,
        'Clouds': -15,
        'Drizzle': 16,
        'Rain': 60,
    }
    return status_to_angle.get(status, 90)

def city_to_geo(city):
    city_to_geo = {
        'Krakow': ("50.0647", "19.9450" ),
        'Stockholm': ("59.334591", "18.063240" ) ,
    }
    return city_to_geo.get(city, ("0","0"))

def import_weather(city):
    print("Showing weather for ", city)
    import requests
    import json
    api_key = "4526d487f12ef78b82b7a7d113faea64"
    lat = city_to_geo(city)[0]
    lon = city_to_geo(city)[1]
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    result = data['current']['weather'][0]['main']
    print("It's ", result, 'in ', city)
    return result



def button1_pressed(active_city, led_Krk, led_Stk):
    print("Switching to Krakow")
    active_city = ("Krakow")
    led_Krk.on()
    led_Stk.off()


def button2_pressed(active_city, led_Krk, led_Stk):
    print("Switching to Stockholm")
    active_city = ("Stocholm")
    led_Krk.off()
    led_Stk.on()


@circuit.run
def main():
    # now just write the code you would use on a real Raspberry Pi

    from time import sleep
    from gpiozero import AngularServo, Button, LED

    servo1 = AngularServo(17,min_angle=-90, max_angle=90)
    
    # possible_status = ['Rain', 'Clear', 'Clouds', 'Drizzle']

    #LED for showig activ city
    led_Krk = LED(22)
    led_Stk = LED(21)
    
    active_city = "Krakow"
    led_Krk.on()

    button1 = Button(11)
    button2 = Button(12)
    button1.when_pressed = lambda : button1_pressed(active_city, led_Krk, led_Stk)
    button2.when_pressed = lambda : button2_pressed(active_city, led_Krk, led_Stk)

    
    while True:
        print("Active city: ", active_city)
        servo1.angle = status_to_angle(import_weather(active_city))
        sleep(3)


    
    

