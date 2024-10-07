import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
import os
from gtts import gTTS  # مكتبة لتحويل النص إلى كلام وحفظه كملف صوتي
import playsound  # مكتبة لتشغيل الملف الصوتي

# Initialize window
root = tk.Tk()
root.geometry('600x500')  # حجم النافذة
root.resizable(0, 0)
root.config(bg='#2c3e50')  # لون الخلفية الداكن
root.title('GetProjects - Speech to Speech')

# Heading
tk.Label(root, text='SPEECH TO SPEECH', font='Helvetica 25 bold', bg='#2c3e50', fg='#ecf0f1').pack(pady=20)
tk.Label(root, text='By GetProjects', font='Helvetica 12 bold', bg='#2c3e50', fg='#ecf0f1').pack(side=tk.BOTTOM, pady=10)

# Text area
text_area = tk.Text(root, width=50, height=10, font='Helvetica 12', bg='#ecf0f1', fg='#2c3e50', relief='flat')
text_area.place(x=20, y=100)

# Recognizer instance
recognizer = sr.Recognizer()

# Language variable (drop-down menu)
language_var = tk.StringVar()
language_var.set('en')  # Default language is English

# Language selection menu
language_menu = tk.OptionMenu(root, language_var, 'en', 'ar')
language_menu.config(width=10, font=('Helvetica', 12), bg='#3498db', fg='#ecf0f1', relief='flat')
language_menu.place(x=20, y=50)

# Function to convert text to speech and save it as an audio file
def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang=language_var.get())  # استخدام اللغة المحددة لتحويل النص إلى صوت
        audio_file = "output_voice.mp3"  # تحديد اسم ملف الصوت
        tts.save(audio_file)  # حفظ الصوت في ملف
        playsound.playsound(audio_file)  # تشغيل الملف الصوتي
        messagebox.showinfo("Success", f"Voice saved as {audio_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Define functions
def speech_to_text():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            # Inform the user to start speaking
            messagebox.showinfo("Information", "Speak Now...")
            audio = recognizer.listen(source)
            selected_language = language_var.get()
            text = recognizer.recognize_google(audio, language=selected_language)  # Use selected language
            text_area.insert(tk.END, text + "\n")
            # Convert text to speech and save it to a file
            text_to_speech(text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I did not understand the audio.")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results. Check your internet connection.")

def file_to_text():
    # Ask user for audio file
    file_path = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[("Audio Files", "*.wav *.mp3 *.flac")]
    )
    if file_path:
        try:
            # Load audio file
            with sr.AudioFile(file_path) as source:
                audio = recognizer.record(source)
                # Recognize speech from the audio file
                selected_language = language_var.get()
                text = recognizer.recognize_google(audio, language=selected_language)  # Use selected language
                text_area.insert(tk.END, text + "\n")
                # Convert text to speech and save it to a file
                text_to_speech(text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I could not understand the audio file.")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results. Check your internet connection.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def reset_text():
    text_area.delete('1.0', tk.END)

def exit_app():
    root.destroy()

# Button animations
def on_enter(e, btn):
    btn['bg'] = '#34495e'  # عند تحريك المؤشر
def on_leave(e, btn):
    btn['bg'] = '#3498db'  # عند إزالة المؤشر

# Button style
button_style = {
    'font': 'Helvetica 15 bold', 
    'width': 15, 
    'bg': '#3498db', 
    'fg': '#ecf0f1', 
    'relief': 'flat', 
    'activebackground': '#2980b9', 
    'activeforeground': '#ecf0f1',
    'bd': 0
}

# Buttons
listen_btn = tk.Button(root, text="RECORD", command=speech_to_text, **button_style)
listen_btn.place(x=50, y=320)
listen_btn.bind("<Enter>", lambda e: on_enter(e, listen_btn))
listen_btn.bind("<Leave>", lambda e: on_leave(e, listen_btn))

upload_btn = tk.Button(root, text="UPLOAD FILE", command=file_to_text, **button_style)
upload_btn.place(x=250, y=320)
upload_btn.bind("<Enter>", lambda e: on_enter(e, upload_btn))
upload_btn.bind("<Leave>", lambda e: on_leave(e, upload_btn))

reset_btn = tk.Button(root, text="RESET", command=reset_text, **button_style)
reset_btn.place(x=50, y=400)
reset_btn.bind("<Enter>", lambda e: on_enter(e, reset_btn))
reset_btn.bind("<Leave>", lambda e: on_leave(e, reset_btn))

exit_btn = tk.Button(root, text="EXIT", command=exit_app, **button_style)
exit_btn.place(x=250, y=400)
exit_btn.bind("<Enter>", lambda e: on_enter(e, exit_btn))
exit_btn.bind("<Leave>", lambda e: on_leave(e, exit_btn))

# Infinite loop to run program
root.mainloop()
