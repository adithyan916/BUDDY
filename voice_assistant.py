import speech_recognition as sr
import pyttsx3
from datetime import datetime
import os
from config import SPEECH_RATE, VOLUME, VOICE_GENDER
from utils import get_greeting, log_command

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.setup_tts_engine()
        self.is_running = True
        self.command_history = []
        
    def setup_tts_engine(self):
        """Configure text-to-speech engine"""
        self.engine.setProperty('rate', SPEECH_RATE)
        self.engine.setProperty('volume', VOLUME)
        
        # Set voice gender
        voices = self.engine.getProperty('voices')
        if VOICE_GENDER == 'female' and len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)
        else:
            self.engine.setProperty('voice', voices[0].id)
    
    def speak(self, text):
        """Convert text to speech and play it"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to user voice and convert to text"""
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=10)
            
            text = self.recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()
            
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that. Could you please repeat?")
            return None
        except sr.RequestError:
            self.speak("Sorry, I'm having trouble connecting to the speech service.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def process_command(self, command):
        """Process user commands"""
        if not command:
            return
        
        log_command(command)
        
        # Time command
        if 'time' in command:
            current_time = datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
        
        # Date command
        elif 'date' in command:
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}")
        
        # Greeting commands
        elif any(word in command for word in ['hello', 'hi', 'hey']):
            greeting = get_greeting()
            self.speak(greeting)
        
        # Exit command
        elif any(word in command for word in ['exit', 'quit', 'bye', 'goodbye']):
            self.speak("Goodbye! Have a great day!")
            self.is_running = False
        
        # Unknown command
        else:
            self.speak("I'm sorry, I don't understand that command yet. Try asking for the time, date, or say hello!")
    
    def run(self):
        """Main loop for the voice assistant"""
        self.speak("Hello! I'm your voice assistant. How can I help you?")
        
        while self.is_running:
            command = self.listen()
            if command:
                self.process_command(command)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()