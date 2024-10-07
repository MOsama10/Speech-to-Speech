import tkinter as tk
from tkinter import filedialog, messagebox
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os

class SpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Arabic Speech Recognition and Synthesis")
        master.geometry("600x500")

        # Define the path of the uploaded file
        self.uploaded_file_path = None

        # Speech-to-Text Section
        self.record_button = tk.Button(master, text="Record Arabic Speech", command=self.record_speech, font=("Arial", 14))
        self.record_button.pack(pady=10)

        self.upload_button = tk.Button(master, text="Upload Audio File", command=self.upload_audio, font=("Arial", 14))
        self.upload_button.pack(pady=10)

        self.transcribe_button = tk.Button(master, text="Transcribe Arabic Speech", command=self.transcribe_speech, font=("Arial", 14))
        self.transcribe_button.pack(pady=10)

        self.transcription_label = tk.Label(master, text="Arabic Transcription will appear here.", font=("Arial", 12), wraplength=500)
        self.transcription_label.pack(pady=20)

        # Text-to-Speech Section
        self.text_entry = tk.Entry(master, width=50, font=("Arial", 14))
        self.text_entry.pack(pady=10)
        self.text_entry.insert(0, "اكتب النص هنا للتحويل إلى صوت")

        self.tts_gtts_button = tk.Button(master, text="Convert Text to Speech (gTTS)", command=self.text_to_speech_gtts, font=("Arial", 14))
        self.tts_gtts_button.pack(pady=10)

        self.tts_pyttsx3_button = tk.Button(master, text="Convert Text to Speech (pyttsx3)", command=self.text_to_speech_pyttsx3, font=("Arial", 14))
        self.tts_pyttsx3_button.pack(pady=10)

    def record_speech(self):
        """Record Arabic speech from the microphone"""
        duration = 5  # seconds
        sample_rate = 44100
        print("Recording Arabic speech...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        wav.write('recorded_audio.wav', sample_rate, audio_data)  # Save as WAV file
        print("Recording complete. Saved as 'recorded_audio.wav'.")
        messagebox.showinfo("Recording", "Recording complete. Saved as 'recorded_audio.wav'.")

    def upload_audio(self):
        """Upload an audio file"""
        self.uploaded_file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")], title="Select an Audio File")
        if self.uploaded_file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.uploaded_file_path}")
            print(f"Uploaded file: {self.uploaded_file_path}")
        else:
            messagebox.showwarning("No File", "No file was selected. Please upload a .wav file.")

    def transcribe_speech(self):
        """Transcribe recorded or uploaded Arabic speech"""
        recognizer = sr.Recognizer()
        audio_file = 'recorded_audio.wav' if not self.uploaded_file_path else self.uploaded_file_path

        try:
            with sr.AudioFile(audio_file) as source:
                print(f"Listening to the audio file: {audio_file}...")
                audio = recognizer.record(source)

            print("Recognizing Arabic speech...")
            text = recognizer.recognize_google(audio, language="ar-SA")
            print(f"Arabic Transcription: {text}")
            self.transcription_label.config(text=f"Transcription: {text}")  # Update label with transcription
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the audio.")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service; {e}")

    def text_to_speech_gtts(self):
        """Convert text to speech using gTTS (Google Text-to-Speech)"""
        text = self.text_entry.get()
        tts = gTTS(text=text, lang='ar')
        output_file = "output_arabic_speech.mp3"
        tts.save(output_file)
        os.system(f"start {output_file}")  # Play the generated speech
        messagebox.showinfo("Success", f"Speech saved to {output_file}")

    def text_to_speech_pyttsx3(self):
        """Convert text to speech using pyttsx3"""
        text = self.text_entry.get()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        # Select Arabic voice if available
        arabic_voice_found = False
        for voice in voices:
            if 'ar' in voice.languages:
                engine.setProperty('voice', voice.id)
                arabic_voice_found = True
                break

        if not arabic_voice_found:
            messagebox.showwarning("Warning", "No Arabic voice found. Defaulting to system voice.")
        
        engine.setProperty('rate', 150)  # Adjust speech rate
        engine.setProperty('volume', 1)  # Set volume to maximum
        engine.say(text)  # Convert text to speech
        engine.runAndWait()  # Play the speech

        messagebox.showinfo("Success", "Speech synthesized successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechApp(root)
    root.mainloop()
