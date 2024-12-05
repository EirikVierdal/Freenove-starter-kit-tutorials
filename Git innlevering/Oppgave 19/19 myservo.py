from machine import Pin, PWM
import time

servo = PWM(Pin(16))
servo.freq(50)


servo.duty_u16(7500)  
time.sleep(2)


servo.duty_u16(5000)  
time.sleep(2)


servo.duty_u16(10000) 
time.sleep(2)

servo.duty_u16(7500)  
time.sleep(2)


servo.duty_u16(5000)  
time.sleep(2)


servo.duty_u16(10000)  
time.sleep(2)

servo.duty_u16(7500)  
time.sleep(2)


servo.duty_u16(5000)  
time.sleep(2)


servo.duty_u16(10000)  
time.sleep(2)

servo.deinit()
