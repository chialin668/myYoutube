#!/usr/bin/env python

import snowboydecoder, sys, signal
from light import Light
from time import sleep
from timeit import default_timer as timer
from recording import Recording
from google_speech import GCPSpeech

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def process():
    led = Light(17)
    led.blink()
    global interrupted 
    interrupted = True

gcp = GCPSpeech()
led = Light(17)

while True:
    interrupted = False
    signal.signal(signal.SIGINT, signal_handler)
    time1 = timer()
    model = 'resources/Murphy.pmdl'
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    time2 = timer()
    print 'dector setup time: ' + str(time2-time1)

    detector.start(detected_callback=process,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)
    detector.terminate()
    time3 = timer()
    print 'decting time: ' + str(time3-time2)

    print 'record for 5 seconds....'
    rec = Recording()
    rec.write_to_file()
    time4 = timer()
    print 'total recording time: ' + str(time4-time3)

    print 'transcribing....'
    gcp.transcribe()
    time5 = timer()
    print 'transcribing time: ' + str(time5-time4)

