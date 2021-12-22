import spidev
import time

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0) # bus:0, dev;0 (CE0:0, CE1:1)

# SPI 통신 속도 설정
spi.max_speed_hz =  100000

# analog -> digital 변환
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 : 0000 1000 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

try:   
    while True:
        ldr_value = analog_read(0) # 0번 채널에서 읽어온 SPI 데이터 (0~1023)
        print("LDR Value: %d" % ldr_value)
        time.sleep(0.5)

finally:
    spi.close()