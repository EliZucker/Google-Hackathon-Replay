# we need to fill this up!
from google.cloud import texttospeech
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import io

def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    client = speech.SpeechClient()
    # [START speech_python_migration_sync_request]
    # [START speech_python_migration_config]
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US')
    # [END speech_python_migration_config]

    # [START speech_python_migration_sync_response]
    response = client.recognize(config, audio)
    # [END speech_python_migration_sync_request]
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    to_return = ""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        to_return += result.alternatives[0].transcript
    return to_return
    # [END speech_python_migration_sync_response]
# [END speech_transcribe_sync]
def textToSpeech(line):
# Instantiates a client
    print 'Converting text to speech'
    tts_client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=line)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
    print 'Before receiving a response'
    response = tts_client.synthesize_speech(synthesis_input, voice, audio_config)
    print 'Received a response and saving it now'
    # The response's audio_content is binary.
    with open('/home/pi/Google-Hackathon-Replay/output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
