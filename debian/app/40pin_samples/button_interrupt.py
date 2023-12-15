#!/usr/bin/env python3
import sys
import signal
import Hobot.GPIO as GPIO
import time

def signal_handler(signal, frame):
    sys.exit(0)

# 定义使用的GPIO通道：
# 12号作为输出，可以点亮一个LED
# 13号作为输出，可以点亮一个LED
# 38号作为输入，可以接一个按钮
led_pin_1 = 12 # BOARD 编码 12
led_pin_2 = 13 # BOARD 编码 13
but_pin = 38   # BOARD 编码 38


# 禁用警告信息
GPIO.setwarnings(False)

# 按下按钮时 LED 2 快速闪烁 5 次
def blink(channel):
    print("Blink LED 2")
    for i in range(5):
        GPIO.output(led_pin_2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin_2, GPIO.LOW)
        time.sleep(0.5)

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup([led_pin_1, led_pin_2], GPIO.OUT)  # LED pins set as output
    GPIO.setup(but_pin, GPIO.IN)  # button pin set as input

    # Initial state for LEDs:
    GPIO.output(led_pin_1, GPIO.LOW)
    GPIO.output(led_pin_2, GPIO.LOW)

    # 把blink函数注册为按钮下降沿事件的中断处理函数
    GPIO.add_event_detect(but_pin, GPIO.FALLING, callback=blink, bouncetime=10)
    # 开始测试， Led1 缓慢闪烁
    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
            # blink LED 1 slowly
            GPIO.output(led_pin_1, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(led_pin_1, GPIO.LOW)
            time.sleep(2)
    finally:
        GPIO.cleanup()  # cleanup all GPIOs

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
