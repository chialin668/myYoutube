#!/usr/bin/env python 
import pyaudio
import wave
from light import Light
from timeit import default_timer as timer
 
class Recording:
    def __init__(self):
        self.CHUNK = 512
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 3
        self.WAVE_FILENAME = "output.wav"
        self.paudio = pyaudio.PyAudio()
        print self.paudio.is_format_supported(input_format=self.FORMAT, input_channels=self.CHANNELS, rate=self.RATE,input_device=2)
        print self.paudio.get_default_input_device_info()
        print self.paudio.get_device_info_by_index(2)
        self.led = Light(17)
 
    def record(self):
        self.led.blink()
        stream = self.paudio.open(format=self.FORMAT,
                                channels=self.CHANNELS,
                                rate=self.RATE,
                                input=True,
                                frames_per_buffer=self.CHUNK,
                                input_device_index=2)
         
        print("*** recording")
        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
          data = stream.read(self.CHUNK)
          frames.append(data)
        print("*** done recording")
        stream.stop_stream()
        stream.close()
        self.paudio.terminate()
        return frames
 
    def write_to_file(self):
        frames = self.record()
        time1 = timer()
        wf = wave.open(self.WAVE_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.paudio.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        time2 = timer()
        print 'saving time: ' + str(time2-time1)

if __name__ == '__main__':
    rec = Recording()
    rec.write_to_file()

