from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

@app.route("/") # 함수 이름은 다 달라야 함.
def home():
    return render_template("led.html")

@app.route("/led/<led_state>")
def led_turn(led_state): # led_state 를 주소로 받아왔으면, 그 값을 함수의 인자로 넣어주어야 함.
    str=led_state.upper()
    if str == 'ON':
        GPIO.output(LED_PIN,1)
        return "LED ON"
    elif str == 'OFF':
        GPIO.output(LED_PIN,0)
        return "LED OFF"
    else:
        return "INPUT ERROR"
        
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',port=9000)
    finally:
        print("clean up")
        GPIO.cleanup()