#!/usr/bin/env python

def run_quickstart():
    print 'importing...'
    import io
    import os
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types

    print 'init client....'
    client = speech.SpeechClient()

    print 'recognizing...'
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        #sample_rate_hertz=16000,
        #language_code='en-US')
        language_code='cmn-Hant-TW')

    print 'about to read the file....'
    file_name = '/home/pi/speech/myYoutube/output.wav'

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    response = client.recognize(config, audio)
    print response
    for result in response.results:
        print(result.alternatives[0].transcript)


if __name__ == '__main__':
    run_quickstart()
