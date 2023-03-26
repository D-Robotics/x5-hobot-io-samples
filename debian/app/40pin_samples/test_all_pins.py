#!/usr/bin/env python3

from __future__ import print_function
import sys
import time

import Hobot.GPIO as GPIO

# 获取所有可以控制的管脚 BOARD 编号
all_pins = list(GPIO.all_pin_data['BOARD'].keys())
all_pins.sort()

# 从命令行参数里面获取需要测试的管脚号序列
if len(sys.argv) > 1:
    all_pins = map(int, sys.argv[1:])

print("All gpio pins: ", all_pins)

# 禁用警告信息
GPIO.setwarnings(False)

# 开始测试，依次拉高拉低管脚，电平保持250毫秒，键盘输入 CTRL-C 测试下一个管脚
for pin in all_pins:
    print("Testing pin %d as OUTPUT; CTRL-C to test next pin" % pin)
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        while True:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.25)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
