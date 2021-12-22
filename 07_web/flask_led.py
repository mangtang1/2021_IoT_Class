from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

@app.route("/")
def home():
    return '''
    <p>Hello, Flask</p>
    <a href="/led/on">LED ON</a>
    <a href="/led/off">LED OFF</a>'''

@app.route("/led/<led_state>")
def led_turn(led_state): # led_state 를 주소로 받아왔으면, 그 값을 함수의 인자로 넣어주어야 함.
    str=led_state.upper()
    GPIO.output(LED_PIN,str=='ON')

    return '''
    <p>LED %s</p>
    <a href="/">Go Home</a>'''%(str)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)