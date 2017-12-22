

lsusb
Bus 001 Device 004: ID 08bb:2902 Texas Instruments PCM2902 Audio Codec

-- mic control
https://diyhacking.com/best-voice-recognition-software-for-raspberry-pi/

alsamixer
   F6
    Choose the USB device
   F5
    Max the input volume

-- record 
  386  rec -r 16000 -c 1 -b 16 -e signed-integer daiko.1.wav trim 0 1
  388  rec -r 16000 -c 1 -b 16 -e signed-integer daiko.2.wav trim 0 1
  390  rec -r 16000 -c 1 -b 16 -e signed-integer daiko.3.wav trim 0 1

-- playback
  385  aplay daiko.1.wav 
