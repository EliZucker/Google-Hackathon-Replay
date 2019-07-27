import cloud_conn
import audiotest2
import sys
import os
import display_on_rpi
import time
import subprocess

def main():
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/replayml-abeb9b1d988e.json"
	count = 0
	subprocess.Popen("sudo python /home/pi/Google-Hackathon-Replay/main_live_transcribe.py", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        print 'after subprocess'
	while True:
		audiotest2.record('audio/input_audio_'+str(count))
		count+=1
if __name__=="__main__":
	main()
