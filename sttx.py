import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from gtts import gTTS
import os

class SpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Speech Recognition and Synthesis")

        # Speech-to-Text Section
        self.record_button = tk.Button(master, text="Record Speech", command=self.record_speech)
        self.record_button.pack(pady=10)

        self.transcribe_button = tk.Button(master, text="Transcribe Speech", command=self.transcribe_speech)
        self.transcribe_button.pack(pady=10)

        self.transcription_label = tk.Label(master, text="Transcription will appear here.")
        self.transcription_label.pack(pady=10)

        # Text-to-Speech Section
        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=10)
        self.text_entry.insert(0, "Enter text to convert to speech")

        self.tts_button = tk.Button(master, text="Convert Text to Speech", command=self.text_to_speech)
        self.tts_button.pack(pady=10)

    def record_speech(self):
        """Record audio from microphone"""
        duration = 5  # seconds
        sample_rate = 44100
        print("Recording...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        wav.write('recorded_audio.wav', sample_rate, audio_data)  # Save as WAV file
        print("Recording complete. Saved as 'recorded_audio.wav'.")

    def transcribe_speech(self):
        """Transcribe recorded speech"""
        recognizer = sr.Recognizer()
        audio_file = 'recorded_audio.wav'
        
        try:
            with sr.AudioFile(audio_file) as source:
                print("Listening to the recorded audio...")
                audio = recognizer.record(source)

            print("Recognizing speech...")
            text = recognizer.recognize_google(audio, language="ar-SA")
            print(f"Arabic Transcription: {text}")
            self.transcription_label.config(text=text)  # Update label with transcription
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the audio.")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service; {e}")

    def text_to_speech(self):
        """Convert text to speech"""
        text = self.text_entry.get()
        tts = gTTS(text=text, lang='ar')
        output_file = "output_arabic_speech.mp3"
        tts.save(output_file)
        os.system(f"start {output_file}")  # Play the generated speech
        messagebox.showinfo("Success", f"Speech saved to {output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechApp(root)
    root.mainloop()
