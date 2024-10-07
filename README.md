# Speech-to-Speech
# Arabic Speech Recognition and Synthesis Application

This application allows users to record Arabic speech, upload audio files for transcription, and convert text to speech using two different libraries: `gTTS` (Google Text-to-Speech) and `pyttsx3`. It provides an easy-to-use graphical user interface built with Tkinter.

## Features

- **Record Arabic Speech:** Users can record their speech using the microphone and save it as a WAV file.
- **Upload Audio Files:** Users can upload existing WAV audio files for transcription.
- **Transcribe Speech:** Converts Arabic speech in recorded or uploaded audio files into text using Google Speech Recognition.
- **Text-to-Speech:** Converts Arabic text into speech using:
  - `gTTS` for generating audio files.
  - `pyttsx3` for immediate playback.

## Requirements

Make sure you have Python installed (preferably Python 3.6 or higher). You can install the required libraries using `pip`. Here’s a list of dependencies:

```bash
pip install sounddevice numpy scipy SpeechRecognition gTTS pyttsx3
