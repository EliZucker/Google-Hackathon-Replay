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
	subprocess.call("python main_live_transcribe", shell=True)
	while True:
		audiotest2.record('/audio/input_audio_'+count)
		count+=1
if __name__=="__main__":
	main()
