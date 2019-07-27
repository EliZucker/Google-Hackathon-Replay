import cloud_conn
import audiotest2
import sys
import os
import display_on_rpi


audiotest2.record(sys.argv[1])
output_str = cloud_conn.transcribe_file(sys.argv[1]+'.wav')
display_on_rpi.init_display()
display_on_rpi.display_text(output_str)
sleep(10)
