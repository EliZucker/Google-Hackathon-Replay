import cloud_conn
import audiotest2
import main_live_transcribe
import sys
import os
import display_on_rpi
import time
import subprocess

def main():
	count = 0
	while True:
		audiotest2.record('audio/input_audio_'+str(count))
		count+=1

if __name__=="__main__":
	main()
