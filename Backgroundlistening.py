import time
import speech_recognition as sr

# function to be called from background thread
def callback(recognizer, audio):
    # Recognize speech from given audio
    try:
        print("Text: " + recognizer.recognize_sphinx(audio_data=audio, language="fr-FR"))
    except sr.UnknownValueError:
        print("Sphinx encoutered an unkown error")
    except sr.RequestError as e:
        print("Sphinx error: {0}".format(e))

    