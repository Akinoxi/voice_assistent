import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit as kit
import wikipedia

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

# Function to get the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}")

# Function to search Wikipedia
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    except Exception as e:
        speak("Sorry, I could not find any information on that.")

# Function to play a song
def play_song(song):
    kit.playonyt(song)

# Main loop for the assistant
def main():
    speak("welcome back boss, how i can help you!")
    
    while True:
        command = recognize_speech()
        
        if command:
            if "hello" in command:
                speak("Hello! How can I assist you?")
            elif "time" in command:
                tell_time()
            elif "play" in command:
                song = command.replace("play", "").strip()
                speak(f"Playing {song}")
                play_song(song)
            elif "search" in command:
                query = command.replace("search", "").strip()
                speak(f"Searching Wikipedia for {query}")
                search_wikipedia(query)
            elif "stop" in command or "exit" in command:
                speak("sure boss, we will meet another oppration!")
                break
            else:
                speak("I'm sorry, I can't help with that.")

if __name__ == "__main__":
    main()