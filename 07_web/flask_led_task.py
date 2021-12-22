from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
RED_LED_PIN = 4
BLUE_LED_PIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN,GPIO.OUT)
GPIO.setup(BLUE_LED_PIN,GPIO.OUT)

@app.route("/")
def home():
    return '''
    <p>Hello, Flask</p>
    <a href="/led/red/on">RED LED ON</a>
    <a href="/led/red/off">RED LED OFF</a>
    <br>
    <a href="/led/blue/on">BLUE LED ON</a>
    <a href="/led/blue/off">BLUE LED OFF</a>'''

@app.route("/led/<led_color>/<led_state>")
def led_turn(led_color, led_state): # led_state 를 주소로 받아왔으면, 그 값을 함수의 인자로 넣어주어야 함.
    
    color_str=led_color.upper()
    state_str=led_state.upper()
    if color_str=='RED' : GPIO.output(RED_LED_PIN,state_str=='ON')
    if color_str=='BLUE' : GPIO.output(BLUE_LED_PIN,state_str=='ON')

    return '''
    <p>%s LED %s</p>
    <a href="/">Go Home</a>'''%(color_str,state_str)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',port=10000)
    
    finally:
        GPIO.cleanup()