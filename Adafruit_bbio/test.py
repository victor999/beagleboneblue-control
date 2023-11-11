import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

#motor STBY
GPIO.setup("P9_41", GPIO.OUT)
GPIO.output("P9_41", GPIO.HIGH)

#motor 1
PWM.start("P9_14", 80)

#motor 2
PWM.start("P9_16", 80)

#motor 3
PWM.start("P8_19", 80)

#motor 4
PWM.start("P8_13", 80)

#motor 1
#GPIO.setup("GPIO2_0", GPIO.OUT)
#GPIO.output("GPIO2_0", GPIO.HIGH)
#GPIO.setup("GPIO0_31", GPIO.OUT)
#GPIO.output("GPIO0_31", GPIO.LOW)

#motor 2
#GPIO.setup("GPIO1_16", GPIO.OUT)
#GPIO.output("GPIO1_16", GPIO.LOW)
#GPIO.setup("GPIO2_17", GPIO.OUT)
#GPIO.output("GPIO2_17", GPIO.HIGH)

#motor 3
GPIO.setup("GPIO2_9", GPIO.OUT)
GPIO.output("GPIO2_9", GPIO.HIGH)
GPIO.setup("GPIO2_8", GPIO.OUT)
GPIO.output("GPIO2_8", GPIO.LOW)


#motor 4
GPIO.setup("GPIO2_6", GPIO.OUT)
GPIO.output("GPIO2_6", GPIO.HIGH)
GPIO.setup("GPIO2_7", GPIO.OUT)
GPIO.output("GPIO2_7", GPIO.LOW)


#GPIO.cleanup()

#motor 1
#GPIO.setup("P9_14", GPIO.OUT)
#GPIO.output("P9_14", GPIO.HIGH)

#motor 2
#GPIO.setup("P9_16", GPIO.OUT)
#GPIO.output("P9_16", GPIO.HIGH)

#motor 3
#GPIO.setup("P8_13", GPIO.OUT)
#GPIO.output("P8_13", GPIO.HIGH)

#motor 4
#GPIO.setup("P8_19", GPIO.OUT)
#GPIO.output("P8_19", GPIO.HIGH)

for i in range(10000):
  print(i)

GPIO.cleanup()
