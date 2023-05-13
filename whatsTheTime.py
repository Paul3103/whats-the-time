from machine import Pin, PWM
import utime

# Initialize buzzer on GPIO pin 18
buzzer = PWM(Pin(18))

buzzer.freq(250)
# Get the current time in seconds
timeStarted = utime.time()
track_time = 0
# Loop to keep track of time and buzz every minute
while True:
    current_time = utime.time()
    # Calculate the number of minutes that have passed
    minutes_passed = (current_time-timeStarted) // 60
    print(minutes_passed)
    # Buzz the buzzer for each minute that has passed
    for i in range(minutes_passed+1):
        buzzer.duty_u16(1005)
        utime.sleep_ms(1000)
        buzzer.duty_u16(0)
        utime.sleep_ms(500)

    # Calculate the remaining seconds until the next minute
    remaining_seconds = 60 - (current_time % 60)
 

    # Wait until the next minute starts
    utime.sleep(remaining_seconds)
