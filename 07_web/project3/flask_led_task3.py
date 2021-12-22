from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_RED_PIN = 4
LED_BLUE_PIN = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_PIN,GPIO.OUT)
GPIO.setup(LED_BLUE_PIN,GPIO.OUT)

@app.route("/") # 함수 이름은 다 달라야 함.
def home():
    return render_template("led3.html")

@app.route("/led/<led_color>/<led_state>")
def led_turn(led_color, led_state): # led_state 를 주소로 받아왔으면, 그 값을 함수의 인자로 넣어주어야 함.
    col=led_color.upper()
    str=led_state.upper()

    if col == 'RED':
        GPIO.output(LED_RED_PIN, str=='ON')
        return "RED LED " + str
    elif col == 'BLUE':
        GPIO.output(LED_BLUE_PIN, str=='ON')
        return "BLUE LED " + str
    else :
        return "INPUT ERROR"
        
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',port=9000)
    finally:
        print("clean up")
        GPIO.cleanup()