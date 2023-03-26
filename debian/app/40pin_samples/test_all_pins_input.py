#!/usr/bin/env python3

from __future__ import print_function
import sys

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

# 读取所有管脚的电平
for pin in all_pins:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    value = GPIO.input(pin)
    print("Pin %d input value %d" % (pin, value))
    GPIO.cleanup()
