import cloud_conn
import audiotest2
import sys
import os
import display_on_rpi
import time
from os import listdir
from os.path import isfile, join


def main():
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/replayml-abeb9b1d988e.json"
	mypath = '/home/pi/Google-Hackathon-Replay/audio/'
	while True:
		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		for file in onlyfiles:
			output_str = cloud_conn.transcribe_file('audio/'+file)
			display_on_rpi.init_display()
			display_on_rpi.display_text(output_str)
			os.remove('audio/'+file)


if __name__=="__main__":
	main()
