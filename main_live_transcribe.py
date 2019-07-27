import cloud_conn
import audiotest2
import sys
import os
import display_on_rpi
import time
from os import listdir
from os.path import isfile, join

#Reads the file where we are storing all transcribed text.
#returns the words that are "seconds" back in time
#We look back seconds*3*8 chars (avg 3 words per second, avg 8 chars per word)
	#Or, however much we have in the buffer if we're not that far yet
#We look back 3*seconds words, from that chunk.
def replay(transcription_file, seconds):
	with open(transcription_file, 'r') as content_file:
    		content = content_file.read()
		max_chars_to_look_back = min(seconds*3*8, len(content))
		replayChunk = content[len(total_transcription)-max_chars_to_look_back:]
		wordsInChunk = replayChunk.split()
		max_words_to_replay = min(seconds*3, len(wordsInChunk))
		return wordsInChunk[len(wordsInChunk)-max_words_to_replay:]

def main():
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/replayml-abeb9b1d988e.json"
	mypath = '/home/pi/Google-Hackathon-Replay/audio/'
	f=open("/home/pi/Google-Hackathon-Replay/log.txt", "a+")
	screen = display_on_rpi.init_display()
	while True:
		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		for file in onlyfiles:
			output_str = cloud_conn.transcribe_file('audio/'+file)
			f.write(" " + output_str)
			display_on_rpi.display_text(output_str, screen)
			os.remove('audio/'+file)

if __name__=="__main__":
	main()
