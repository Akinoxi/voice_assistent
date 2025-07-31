# Voice Assistant Project

This is a simple voice assistant project built using Python and Flask. It uses speech recognition to convert audio input to text and text-to-speech to respond.

## Setup

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate      # On Linux/Mac
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

## Usage

Send a POST request to `/voice` endpoint with an audio file (wav format) under the key `audio`. The server will respond with the recognized text and speak the response.

## Notes

- Make sure your microphone or audio input device is working properly.
- The app uses Google's speech recognition service, so an internet connection is required.
- `pyaudio` may require additional system dependencies to be installed.
