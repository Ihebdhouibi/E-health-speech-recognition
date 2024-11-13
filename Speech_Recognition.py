from os import path
import speech_recognition as sr

# First try converting microphone voice to text
#r = sr.Recognizer()
#with sr.Microphone() as source:
#    print("You have the stage!")
#    audio = r.listen(source)
    
    # Recognize speech using Sphinx | Offline 
#    try:
#        print("Sphinx thinks you said: " + r.recognize_sphinx(audio_data=audio))
#    except sr.UnknownValueError:
#        print("Sphinx encoutered an unkown error")
#    except sr.RequestError as e:
#        print("Sphinx error: {0}".format(e))

# Converting audio file to text
audio_file = "data\harvard2.wav"
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)

# recognize audio using Sphinx | Offline 
try:
    print("Sphinx thinks you said: " + r.recognize_sphinx(audio_data=audio, language="fr-FR"))
except sr.UnknownValueError:
    print("Sphinx could not understand audio file given")
except sr.RequestError as e:
    print("Sphinx error:  {0}".format(e))