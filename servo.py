import RPi.GPIO as GPIO    
import time                

pin 	= 16
sleep   = 0.5
CENTER 	= 7.5
LEFT90  = 2.5
LEFT45  = 4.5
RIGHT90 = 12.5
RIGHT45 = 10.5

class Servo:   
   def __init__(self):
      GPIO.setmode(GPIO.BCM)   
      GPIO.setup(pin,GPIO.OUT) 
      self.p = GPIO.PWM(pin,50)
      self.p.start(CENTER)        
      time.sleep(sleep)        
   def move(self, position):
      self.p.ChangeDutyCycle(position)
      time.sleep(sleep)        
   def moveToCenter(self):
      self.move(CENTER)    
   def moveToLeft90(self):
      self.move(LEFT90)    
   def moveToLeft45(self):
      self.move(LEFT45)    
   def moveToRight45(self):
      self.move(RIGHT45)    
   def moveToRight90(self):
      self.move(RIGHT90) 
   def __del__(self):
      self.p.stop()
      GPIO.cleanup()  


servo = Servo()
servo.moveToLeft90() 
servo.moveToLeft45() 
servo.moveToCenter() 
servo.moveToRight45() 
servo.moveToRight90() 
