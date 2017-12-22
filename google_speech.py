#!/usr/bin/env python

import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class GCPSpeech:

    def __init__(self):
        print 'Init Google Speech client....'
        self.client = speech.SpeechClient()

        self.config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            #sample_rate_hertz=16000,
            #language_code='en-US')
            language_code='cmn-Hant-TW')

    def transcribe(self):
        print 'About to read the wav file....'
        file_name = '/home/pi/speech/myYoutube/output.wav'

        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        response = self.client.recognize(self.config, audio)
        print response
        for result in response.results:
            print(result.alternatives[0].transcript)


if __name__ == '__main__':
    gcp = GCPSpeech()
    gcp.transcribe()
