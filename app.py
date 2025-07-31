from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import tempfile
import os

app = Flask(__name__)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/voice', methods=['POST'])
def voice():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']

    # Save the audio file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
        audio_file.save(temp_audio.name)
        temp_filename = temp_audio.name

    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_filename) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        response_text = f"You said: {text}"
        # Speak the response text
        speak_text(response_text)
    except sr.UnknownValueError:
        response_text = "Sorry, I could not understand the audio."
    except sr.RequestError:
        response_text = "Sorry, the speech recognition service is unavailable."

    # Remove the temporary audio file
    os.remove(temp_filename)

    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
