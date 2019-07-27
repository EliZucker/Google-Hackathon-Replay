import cloud_conn
import audiotest2
import sys
import display_on_rpi
import time
from os import listdir, remove, environ
from os.path import isfile, join

def main():
	# remove("/home/pi/Google-Hackathon-Replay/text/log.txt")
	environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/replayml-abeb9b1d988e.json"
	mypath = '/home/pi/Google-Hackathon-Replay/audio/'
	log_file=open("/home/pi/Google-Hackathon-Replay/text/log.txt", "w")
	while True:
		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		for file in onlyfiles:
			output_str = cloud_conn.transcribe_file('audio/'+file)
			log_file.write(" " + output_str)
			remove('audio/'+file)

if __name__=="__main__":
	main()

