import network
import ntptime
import time
from machine import Pin

ssid = "ssid"
password = "password"

#integrated led
led = Pin("LED", Pin.OUT)

led.off()

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for Wi-Fi connection
while not wlan.isconnected():
    time.sleep(1)

print("Connected to Wi-Fi")
led.on()
time.sleep(2)
led.off()

# Sync time with NTP server
try:
    ntptime.settime()  
    print("Time synced with NTP server")
except:
    print("Failed to sync time")

led.on()
time.sleep(2)
led.off()


local_offset_hours = -5
local_time = time.localtime(time.time() + local_offset_hours * 3600)
print("Local time:", local_time)

# Code to control the pump
pump = Pin(20, Pin.OUT)
sensor = Pin(16, Pin.IN)

while True:
    current_time = time.localtime(time.time() + local_offset_hours * 3600)
    hour = current_time[3]
    if (sensor.value() == 1) and (8 < hour <= 20):
        pump.value(1)
        time.sleep(5)
        pump.value(0)
    
    time.sleep(2)

