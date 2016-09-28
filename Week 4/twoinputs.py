#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#GPIO
GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
LED = 7
BUTTON = 11

print "Distance Measurement:"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

GPIO.output(TRIG, True)
print "Waiting for sensor "
time.sleep(2)

def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return  


def getDistance():
    GPIO.output(TRIG, True)
    time.sleep(0.1)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    global distance
    distance = pulse_duration*17150
    distance = round(distance, 2)
    print "Distance:", distance, "cm"

    global input
    input = GPIO.input(BUTTON)
    print input
    return

def emailFunction():        
    fromaddr = "****"
    toaddr = "****"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Human detected"


    body = "Human found on Planet Earth. Human at a distance of "+ distance+ " cm"
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "****")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return

while True:
        getDistance()
        if distance < 10:
            print "Human detected"
            blink(LED)
        if input == 1:
            emailFunction()
    
            









