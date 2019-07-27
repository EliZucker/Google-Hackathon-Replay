import cloud_conn
import audiotest2
import sys
import os
import display_on_rpi
import time
from os import listdir
from os.path import isfile, join
from pitftgpio import PiTFT_GPIO
import subprocess

#Reads the file where we are storing all transcribed text.
#returns the words that are "seconds" back in time
#We look back seconds*3*8 chars (avg 3 words per second, avg 8 chars per word)
	#Or, however much we have in the buffer if we're not that far yet
#We look back 3*seconds worods, from that chunk.
def replay(transcription_file, seconds):
	# with open(transcription_file, 'r', os.O_NONBLOCK) as content_file:
 #    		content = content_file.read()
 	fil = open(transcription_file, 'r', os.O_NONBLOCK)
 	content = fil.read()
 	fil.close()
	max_chars_to_look_back = min(seconds*3*8, len(content))
	replayChunk = content[len(content)-max_chars_to_look_back:]
	wordsInChunk = replayChunk.split()
	max_words_to_replay = min(seconds*3, len(wordsInChunk))
	return " ".join(wordsInChunk[len(wordsInChunk)-max_words_to_replay:])

def save_review_to_file(text_to_save):
	mypath = '/home/pi/Google-Hackathon-Replay/review/'
	f = open(mypath+str(time.time()), "w")
	# print text_to_save
	f.write(text_to_save)
	f.close()


def main():
	time.sleep(1)
	pitft = PiTFT_GPIO(v2=True) 
	screen = display_on_rpi.init_display()
	mypath = '/home/pi/Google-Hackathon-Replay/review/'
	resetReviewLog = True
	reviewFileIter = iter([f for f in listdir(mypath) if isfile(join(mypath, f))])
	while True:
		string_to_display = ''
		if pitft.Button1:
			print "Button 1 pressed - screen off"
			string_to_display = replay("/home/pi/Google-Hackathon-Replay/text/log.txt", 3)
			save_review_to_file(string_to_display)
			display_on_rpi.init_display()
			display_on_rpi.display_text(string_to_display, screen)
			display_on_rpi.draw_file_browsing_interface(screen)
			resetReviewLog = True
			time.sleep(0.1)
		elif pitft.Button2:
			print "Button 2 pressed - screen on"
			string_to_display = replay("/home/pi/Google-Hackathon-Replay/text/log.txt", 6)
			save_review_to_file(string_to_display)
			display_on_rpi.init_display()
			display_on_rpi.display_text(string_to_display, screen)
			display_on_rpi.draw_file_browsing_interface(screen)
			resetReviewLog = True
			time.sleep(0.1)
		elif pitft.Button3:
			print "Button 3 pressed"
			if resetReviewLog:
				resetReviewLog = False
				reviewFileIter = iter([f for f in listdir(mypath) if isfile(join(mypath, f))])
			try:
				file = next(reviewFileIter)
				if file:
					string_to_display = open(mypath+file).read()
					print string_to_display + ' ' +file
					display_on_rpi.init_display()
					display_on_rpi.display_text(string_to_display, screen)
					display_on_rpi.draw_file_browsing_interface(screen)
					#cloud_conn.textToSpeech(string_to_display)
				time.sleep(0.1)
			except Exception as e:
				reviewFileIter = iter([f for f in listdir(mypath) if isfile(join(mypath, f))])
				print "reached end no more printing"
		elif pitft.Button4:
			print "Button 4 pressed"
			time.sleep(0.1)
		else:
			string_to_display = replay("/home/pi/Google-Hackathon-Replay/text/log.txt", 3)
			save_review_to_file(string_to_display)
			display_on_rpi.init_display()
			display_on_rpi.display_text(string_to_display, screen)
			display_on_rpi.draw_file_browsing_interface(screen)
			resetReviewLog = True
			time.sleep(0.1)

if __name__=="__main__":
	os.system('sudo rm -rf review/')
	os.system('sudo mkdir review')
	subprocess.Popen("sudo python /home/pi/Google-Hackathon-Replay/main_live_transcribe.py", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	subprocess.Popen("sudo python /home/pi/Google-Hackathon-Replay/Main.py", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
	main()
