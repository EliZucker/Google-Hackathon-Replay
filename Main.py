import cloud_conn
import audiotest2
import main_live_transcribe
import sys
import os
import display_on_rpi
import time
import subprocess
from pitftgpio import PiTFT_GPIO

def main():
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/replayml-abeb9b1d988e.json"
        pitft = PiTFT_GPIO(v2=True) 
	count = 0
	subprocess.Popen("sudo python /home/pi/Google-Hackathon-Replay/main_live_transcribe.py", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	while True:
        if pitft.Button1:
            print "Button 1 pressed - screen off"
            pitft.Backlight(False)
            string_for_audio = main_live_transcribe.replay("/home/pi/Google-Hackathon-Replay/log.txt", 5)
            #Play audio
        if pitft.Button2:
            print "Button 2 pressed - screen on"
            pitft.Backlight(True) 
        if pitft.Button3:
            print "Button 3 pressed"
        if pitft.Button4:
            print "Button 4 pressed"
		audiotest2.record('audio/input_audio_'+str(count))
		count+=1
if __name__=="__main__":
	main()
