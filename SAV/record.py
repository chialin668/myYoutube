#!/usr/bin/env python 

import pyaudio
import wave
 
CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
 
p = pyaudio.PyAudio()
 
print p.is_format_supported(input_format=FORMAT, input_channels=CHANNELS, rate=RATE,input_device=2)
print p.get_default_input_device_info()
print p.get_device_info_by_index(2)
 
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=2)
 
print("* recording")
 
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
  data = stream.read(CHUNK)
  frames.append(data)
 
print("* done recording")
 
stream.stop_stream()
stream.close()
p.terminate()
 
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
