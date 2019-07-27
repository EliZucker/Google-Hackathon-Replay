import cloud_conn
import audiotest2
import display_on_rpi


audiotest2.record(sys.argv[1])
output_str = cloud_conn.transcribe_file(sys.argv[1]+'.wav')


display_on_rpi(output_str)
