# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# 라이브러리 임포트 하기
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# 핀 지정
RESET_PIN = digitalio.DigitalInOut(board.D4)

# I2C 연결하기
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=RESET_PIN)

# oled 초기화 하기
oled.fill(0)
oled.show()

# oled 캠버스 만들기
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# 폰트 불러오기
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)

def draw_OLED(**args):
    # 글자 쓰기
    
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)


    if args.get('pos') == None: args['pos']=(0,0)
    if args.get('text') == None: args['text']="         "
    if args.get('fill') == None: args['fill']=200
    draw.text(args['pos'], args['text'], font=font2, fill=args['fill'])

    # 이미지 출력하기
    oled.image(image)
    oled.show()