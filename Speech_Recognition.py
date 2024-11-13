from os import path
import speech_recognition as sr

# First try converting microphone voice to text
r = sr.Recognizer()
with sr.Microphone() as source:
    print("You have the stage!")
    audio = r.listen(source)
    r.adjust_for_ambient_noise(source)
   # Recognize speech using Sphinx | Offline 
    try:
        print("Whisper thinks you said: " + r.recognize_whisper(audio_data=audio,
                                                                   language='fr',
                                                                   model="medium"))
        # models to use ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en',
        #  'medium', 'large-v1', 'large-v2', 'large-v3', 'large', 'large-v3-turbo', 'turbo']
    except sr.UnknownValueError:
        print("Whisper encoutered an unkown error")
    except sr.RequestError as e:
        print("Whisper error: {0}".format(e))

# Converting audio file to text
#audio_file = "data\harvard2.wav"
#r = sr.Recognizer()
#with sr.AudioFile(audio_file) as source:
#    audio = r.record(source)

# recognize audio using Sphinx | Offline 
#try:
#    print("Sphinx thinks you said: " + r.recognize_s
# phinx(audio_data=audio, language="fr-FR"))
#except sr.UnknownValueError:
#    print("Sphinx could not understand audio file given")
#except sr.RequestError as e:
#    print("Sphinx error:  {0}".format(e))