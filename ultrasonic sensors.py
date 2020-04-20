#for ULtrasonic sensors
GPIO.setmode(GPIO.BOARD)

GPIO_trigger1 = 29      #1st left sensor
GPIO_echo1 = 31

GPIO_trigger2 = 36      #2nd left sensor
GPIO_echo2 = 37

GPIO_trigger3 = 33      #3rd left sensor
GPIO_echo3 = 35

Motor1b=18  #Left Motor
Motor1e=22

Motor2b=21  #Right Motor
Motor2e=19

led=13  #for lighting when object founded


GPIO.setup(GPIO_trigger1,GPIO.OUT)  # trigger
GPIO.setup(GPIO_echo1,GPIO.IN)      # echo
GPIO.setup(GPIO_trigger2,GPIO.OUT)  # trigger
GPIO.setup(GPIO_echo2,GPIO.IN)      #echo
GPIO.setup(GPIO_trigger3,GPIO.OUT)  # trigger
GPIO.setup(GPIO_echo3,GPIO.IN)      #echo
GPIO.setup(led,GPIO.OUT)        #LED

# ALL trigger set to false
GPIO.output(GPIO_trigger1, False)
GPIO.output(GPIO_trigger2, False)
GPIO.output(GPIO_trigger3, False)

# Allow ing modeule to settle
def sonar(GPIO_trigger,GPIO_echo):
      start=0
      stop=0
      # Set pins as output and input
      GPIO.setup(GPIO_trigger,GPIO.OUT)  # trigger
      GPIO.setup(GPIO_echo,GPIO.IN)      # echo
     
      # Set trigger to False (Low)
      GPIO.output(GPIO_trigger, False)
     
      # Allow module to settle
      time.sleep(0.01)
           
      #while distance > 5:
      #Send 10us pulse to trigger
      GPIO.output(GPIO_trigger, True)
      time.sleep(0.00001)
      GPIO.output(GPIO_trigger, False)
      begin = time.time()
      while GPIO.input(GPIO_echo)==0 and time.time()<begin+0.05:
            start = time.time()
     
      while GPIO.input(GPIO_echo)==1 and time.time()<begin+0.1:
            stop = time.time()
     
      # pulse length
      elapsed = stop-start
      distance = elapsed * 34000
      distance = distance / 2
     
      print "Distance : %.1f" % distance
      return distance

GPIO.setup(Motor1b, GPIO.OUT)
GPIO.setup(Motor1e, GPIO.OUT)

GPIO.setup(Motor2b, GPIO.OUT)
GPIO.setup(Motor2e, GPIO.OUT)

def forward():
      GPIO.output(Motor1b, GPIO.HIGH)
      GPIO.output(Motor1e, GPIO.LOW)
      GPIO.output(Motor2b, GPIO.HIGH)
      GPIO.output(Motor2e, GPIO.LOW)
     
def reverse():
      GPIO.output(Motor1b, GPIO.LOW)
      GPIO.output(Motor1e, GPIO.HIGH)
      GPIO.output(Motor2b, GPIO.LOW)
      GPIO.output(Motor2e, GPIO.HIGH)
     
def rightturn():
      GPIO.output(Motor1b,GPIO.LOW)
      GPIO.output(Motor1e,GPIO.HIGH)
      GPIO.output(Motor2b,GPIO.HIGH)
      GPIO.output(Motor2e,GPIO.LOW)
     
def leftturn():
      GPIO.output(Motor1b,GPIO.HIGH)
      GPIO.output(Motor1e,GPIO.LOW)
      GPIO.output(Motor2b,GPIO.LOW)
      GPIO.output(Motor2e,GPIO.HIGH)

def stop():
      GPIO.output(Motor1e,GPIO.LOW)
      GPIO.output(Motor1b,GPIO.LOW)
      GPIO.output(Motor2e,GPIO.LOW)
      GPIO.output(Motor2b,GPIO.LOW)
