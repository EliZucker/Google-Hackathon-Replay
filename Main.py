import cloud_conn
import audiotest2
import sys
import os
import display_on_rpi
import time


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/replayml-abeb9b1d988e.json"
audiotest2.record(sys.argv[1])
output_str = cloud_conn.transcribe_file(sys.argv[1]+'.wav')
display_on_rpi.init_display()
display_on_rpi.display_text(output_str)
time.sleep(10)
