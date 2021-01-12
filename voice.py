import speech_recognition, pyaudio

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
     print("say something!")
     audio = recognizer.listen(source)

print("Google Speech Recognition thinks you said: ")    
print(recognizer.recognize_google(audio))