#!/usr/bin/env python3
import sys
import signal
import Hobot.GPIO as GPIO
import time

def signal_handler(signal, frame):
    sys.exit(0)

# 定义使用的GPIO通道：
# 36号作为输出，可以点亮一个LED
# 37号作为输入，可以接一个按钮
led_pin = 36 # BOARD 编码 36
but_pin = 37 # BOARD 编码 37

# 禁用警告信息
GPIO.setwarnings(False)

def main():
    prev_value = None

    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(led_pin, GPIO.OUT)  # LED pin set as output
    GPIO.setup(but_pin, GPIO.IN)  # Button pin set as input

    # Initial state for LEDs:
    GPIO.output(led_pin, GPIO.LOW)
    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
            curr_value = GPIO.input(but_pin)
            if curr_value != prev_value:
                GPIO.output(led_pin, curr_value)
                prev_value = curr_value
                print("Outputting {} to Pin {}".format(curr_value, led_pin))
            time.sleep(1)
    finally:
        GPIO.cleanup()  # cleanup all GPIO

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
