# DS3231 library for micropython
# tested on ESP8266
#
# Author: Sebastian Maerker
# License: mit
# 
# only 24h mode is supported
#
# example on how to set and use the alarm on the DS3231

import DS3231micro
import machine
import time

#initialize DS3231
rtc = DS3231micro.DS3231(5, 4)

# set time to 2019, November, 23, Monday, 19 h, 50 min, 0 sec
rtc.setDateTime(19, 11, 23, 1, 19, 50, 0)

# set alarm to go off every second
rtc.setAlarm1(0, 22, 50, 10, "everySecond")

# turn on interrupt routine
rtc.turnOnAlarmIR(1)

# PIN14 on controller becomes input pin to sense the IR pin
inputPinIR = machine.Pin(14, machine.Pin.IN)

# IR should be triggert every second for 5 seconds and is turned off afterwards
print("interrupt via pin")

for each in range(10):
    if(inputPinIR.value() == False):
        print("triggert")
        rtc.resetAlarmFlag(1)
    time.sleep(0.5)

# IR should be tiggert every second for 5 seconds
print("interrupt via internal function")

for each in range(10):
    if(rtc.alarmTriggert(1)):
        print("triggert")
    time.sleep(0.5)
