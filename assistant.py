import os
import datetime
import webbrowser
import warnings

import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import pyjokes

from dotenv import load_dotenv
from openai import OpenAI

# ==========================================
# Remove Warnings
# ==========================================

warnings.filterwarnings("ignore")

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

# ==========================================
# OpenAI Client
# ==========================================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ==========================================
# Initialize Voice Engine
# ==========================================

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 175)

# ==========================================
# Speak Function
# ==========================================

def speak(text):

    print(f"\nAssistant: {text}")

    engine.say(text)

    engine.runAndWait()

# ==========================================
# AI Response Function
# ==========================================

def ask_ai(prompt):

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a smart AI productivity assistant. "
                        "Give concise and useful responses."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            max_tokens=250

        )

        answer = response.choices[0].message.content

        return answer

    except Exception as e:

        return f"Error: {str(e)}"

# ==========================================
# Wake Word Detection
# ==========================================

def wait_for_wake_word():

    recognizer = sr.Recognizer()

    print("\nAssistant is waiting for wake word...")

    while True:

        try:

            with sr.Microphone() as source:

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = recognizer.listen(source)

                wake_command = recognizer.recognize_google(audio)

                wake_command = wake_command.lower()

                print(f"\nHeard: {wake_command}")

                # ==================================
                # Wake Word + Command Together
                # ==================================

                if 'hey assistant' in wake_command:

                    command = wake_command.replace(
                        'hey assistant',
                        ''
                    ).strip()

                    speak('Yes Manvika')

                    return command

                elif 'hello assistant' in wake_command:

                    command = wake_command.replace(
                        'hello assistant',
                        ''
                    ).strip()

                    speak('Yes Manvika')

                    return command

        except:

            pass

# ==========================================
# Assistant Commands
# ==========================================

def run_assistant(command):

    # ======================================
    # Greetings
    # ======================================

    if 'hello' in command:

        speak('Hello Manvika, how can I help you today?')

    # ======================================
    # Open Websites
    # ======================================

    elif 'open youtube' in command:

        speak('Opening YouTube')

        webbrowser.open('https://youtube.com')

    elif 'open google' in command:

        speak('Opening Google')

        webbrowser.open('https://google.com')

    elif 'open whatsapp' in command:

        speak('Opening WhatsApp')

        webbrowser.open('https://web.whatsapp.com')

    elif 'open instagram' in command:

        speak('Opening Instagram')

        webbrowser.open('https://instagram.com')

    elif 'open linkedin' in command:

        speak('Opening LinkedIn')

        webbrowser.open('https://linkedin.com')

    elif 'open github' in command:

        speak('Opening GitHub')

        webbrowser.open('https://github.com')

    elif 'open spotify' in command:

        speak('Opening Spotify')

        webbrowser.open('https://spotify.com')

    elif 'open netflix' in command:

        speak('Opening Netflix')

        webbrowser.open('https://netflix.com')

    elif 'open snapchat' in command:

        speak('Opening Snapchat')

        webbrowser.open('https://web.snapchat.com')

    elif 'open chat g p t' in command:

        speak('Opening ChatGPT')

        webbrowser.open('https://chatgpt.com')

    # ======================================
    # Open Applications
    # ======================================

    elif 'open code' in command:

        speak('Opening Visual Studio Code')

        os.startfile(
            "C:\\Users\\bhano\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        )

    elif 'open chrome' in command:

        speak('Opening Chrome')

        os.startfile(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        )

    elif 'open calculator' in command:

        speak('Opening Calculator')

        os.system('calc')

    elif 'open notepad' in command:

        speak('Opening Notepad')

        os.system('notepad')

    elif 'open paint' in command:

        speak('Opening Paint')

        os.system('mspaint')

    elif 'open command prompt' in command:

        speak('Opening Command Prompt')

        os.system('start cmd')

    elif 'open file explorer' in command:

        speak('Opening File Explorer')

        os.system('explorer')

    elif 'open camera' in command:

        speak('Opening Camera')

        os.system('start microsoft.windows.camera:')

    # ======================================
    # Search Features
    # ======================================

    elif 'search' in command:

        query = command.replace('search', '').strip()

        speak(f'Searching Google for {query}')

        webbrowser.open(
            f'https://www.google.com/search?q={query}'
        )

    elif 'wikipedia' in command:

        query = command.replace('wikipedia', '').strip()

        if query == "":

            speak('What should I search on Wikipedia?')

        else:

            speak(f'Searching Wikipedia for {query}')

            try:

                result = wikipedia.summary(query, 2)

                speak(result)

            except:

                speak('Sorry, I could not find information.')

    # ======================================
    # Play Songs / Videos
    # ======================================

    elif 'play' in command:

        song = command.replace('play', '').strip()

        speak(f'Playing {song}')

        pywhatkit.playonyt(song)

    # ======================================
    # Productivity Features
    # ======================================

    elif 'time' in command:

        current_time = datetime.datetime.now().strftime('%I:%M %p')

        speak(f'Current time is {current_time}')

    elif 'date' in command:

        current_date = datetime.datetime.now().strftime('%d %B %Y')

        speak(f'Today is {current_date}')

    elif 'joke' in command:

        joke = pyjokes.get_joke()

        speak(joke)

    elif 'motivate me' in command:

        motivation = (
            "Success comes from consistency and continuous learning. "
            "Keep building projects and improving your skills."
        )

        speak(motivation)

    elif 'study tip' in command:

        tip = (
            "Study in focused sessions with short breaks. "
            "Practice projects daily for better learning."
        )

        speak(tip)

    # ======================================
    # Computer Controls
    # ======================================

    elif 'shutdown computer' in command:

        speak('Shutting down computer')

        os.system('shutdown /s /t 5')

    elif 'restart computer' in command:

        speak('Restarting computer')

        os.system('shutdown /r /t 5')

    elif 'lock computer' in command:

        speak('Locking computer')

        os.system(
            'rundll32.exe user32.dll,LockWorkStation'
        )

    # ======================================
    # Stop Assistant
    # ======================================

    elif 'stop assistant' in command:

        speak('Stopping assistant')

        exit()

    # ======================================
    # AI Smart Responses
    # ======================================

    else:

        speak('Thinking...')

        answer = ask_ai(command)

        speak(answer)

# ==========================================
# Assistant Startup
# ==========================================

speak('Ultimate AI Voice Assistant Started Successfully')

# ==========================================
# Main Loop
# ==========================================

while True:

    command = wait_for_wake_word()

    if command:

        run_assistant(command)