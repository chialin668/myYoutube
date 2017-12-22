#!/usr/bin/env python

import snowboydecoder
import sys
import signal
from light import Light

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def process():
    led = Light(17)
    led.blink()

model = 'resources/Murphy.pmdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
led = Light(17)
detector.start(detected_callback=process,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
