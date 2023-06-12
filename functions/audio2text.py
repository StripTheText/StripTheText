# Import of required libraries
import pathlib
import whisper
import tempfile
import os
from audiorecorder import audiorecorder
import streamlit as st


# Define the function to convert audio to text
@st.cache_data
def fun_audio_to_text(
        audio2transcript: audiorecorder = None) -> str:
    """
    Function to convert audio to text using the Open AI-Whisper Model
    :param audio2transcript: Audio which needs to be transcribed
    :return: str: Transcribed text
    """
    # Download the Open AI-Whisper Model
    whisper_model = whisper.load_model(
        name="base.en",
        download_root=str(pathlib.Path.joinpath(pathlib.Path.cwd(), "models", "whisper")),
        in_memory=False
    )
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
        fp.write(audio2transcript.tobytes())
        temp_filename = fp.name

    result = whisper_model.transcribe(audio=temp_filename)

    os.remove(temp_filename)

    # Return the result of the transcription
    if result["text"] is not None:
        return result["text"]
    else:
        return "Warning: No text found in the audio file!"
