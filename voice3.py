import re
import speech_recognition

# obtain audio from the microphone
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print ("Say Something!")
    audio = recognizer.listen(source)

# Recognize speech using Google Speech Recognition
words = recognizer.recognize_google(audio)

# Respond to speech 
matches = re.search("my name is (.*)", words)
if matches:
    print("Hey, {matches[1]}.")
else:
    print("Hey, you.")