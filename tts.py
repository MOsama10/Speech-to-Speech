import pyttsx3

def list_voices():
    """List all available voices on the system."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"Voice {index}:")
        print(f" - ID: {voice.id}")
        print(f" - Name: {voice.name}")
        print(f" - Languages: {voice.languages}")
        print()

def text_to_speech(text, lang='en'):
    """Convert text to speech using the specified language."""
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    
    # Select voice based on the language
    if lang == 'ar':
        arabic_voice_found = False
        for voice in voices:
            if 'ar' in voice.languages:  # Check if the voice supports Arabic
                engine.setProperty('voice', voice.id)
                arabic_voice_found = True
                break
        if not arabic_voice_found:
            print("No Arabic voice found. Please check your installed voices.")
            return
    else:  # Default to English
        for voice in voices:
            if 'en' in voice.languages:  # Check if the voice supports English
                engine.setProperty('voice', voice.id)
                break

    engine.setProperty('rate', 150)  # Adjust speech rate
    engine.setProperty('volume', 1)   # Set volume to maximum
    engine.say(text)                  # Convert text to speech
    engine.runAndWait()               # Play the speech

if __name__ == "__main__":
    list_voices()  # List available voices
    arabic_text = "ازيك عامل ايه"  # Arabic text
    english_text = "Hello, how are you?"  # English text
    
    # Test text-to-speech for Arabic
    print("Testing Arabic TTS:")
    text_to_speech(arabic_text, lang='ar')  
    
    # Test text-to-speech for English
    print("Testing English TTS:")
    text_to_speech(english_text, lang='en')  
