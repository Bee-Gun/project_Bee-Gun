import Jetson.GPIO as GPIO
import time

SERVO_PIN_1 = 32
SERVO_PIN_2 = 33

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN_1, GPIO.OUT)
GPIO.setup(SERVO_PIN_2, GPIO.OUT)

pwm_1 = GPIO.PWM(SERVO_PIN_1, 50)
pwm_2 = GPIO.PWM(SERVO_PIN_2, 50)   # 서보모터를 제어하기 위한 주파수. 50Hz = 주기20ms

pwm_1.start((1./18.)*100 + 2)
pwm_2.start((1./18.)*40 + 2)

for i in range(0,20):
    desiredPosition_1 = float(input('Move X : '))
    desiredPosition_2 = float(input('Move Y : '))
    DC_1 = (1./18.)*(desiredPosition_1) + 2
    DC_2 = (1./18.)*(desiredPosition_2) + 2
    pwm_1.ChangeDutyCycle(DC_1)
    pwm_2.ChangeDutyCycle(DC_2)

pwm_1.stop()
pwm_2.stop()
GPIO.cleanup()




