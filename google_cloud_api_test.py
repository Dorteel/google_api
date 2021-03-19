# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import types
from google.cloud.speech import enums
import os
import io


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/dorte/PycharmProjects/asr/mark_key.json'

# Instantiates a client
print("Instantiating client...")
client = speech.SpeechClient()
print("...done")

print("Setting up the audio file...")
with io.open('testing1.wav', 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
print("...done")

# The name of the audio file to transcribe
# gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
#
# audio = speech.RecognitionAudio(uri=gcs_uri)
print("Setting up config ...")
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US"
)
print("...done")

# Detects speech in the audio file
print("Detects speech in the audio file...")
response = client.recognize(config=config, audio=audio)
print("...done")

print("Printing the result...")
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
print("...done")