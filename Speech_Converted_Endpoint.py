from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydub import AudioSegment
import os
import tempfile

app = FastAPI()

@app.get("/transcribe-audio/")
async def read_voice(file: UploadFile = File()):
     # Verify the file is an audio file
    if not file.content_type.startswith("audio"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an audio file.")
    
    # Save the uploaded audio file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        temp_audio_file.write(await file.read())
        temp_audio_path = temp_audio_file.name
    
    # Initialize recognizer and transcribe audio
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_google(audio_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio file: {e}")
    finally:
        os.remove(temp_audio_path)  # Clean up the temporary file

    return {"transcription": transcription}