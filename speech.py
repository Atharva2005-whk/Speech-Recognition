from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import queue
import sys
import os

# Constants
MODEL_PATH = "vosk-model-en-us-0.22-lgraph"
SAMPLE_RATE = 16000
BLOCK_SIZE = 8000

# Initialize queue
q = queue.Queue()

# Load Vosk model
if not os.path.exists(MODEL_PATH):
    sys.exit(f"Model not found at '{MODEL_PATH}'. Please check the path.")
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

# Callback for audio stream
def callback(indata, frames, time, status):
    if status:
        print("Audio Status:", status, file=sys.stderr)
    q.put(bytes(indata))

# Main listening function
def listen():
    print("Listening (Vosk)... Press Ctrl+C to stop.")

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        dtype='int16',
        channels=1,
        callback=callback
    ):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()
                if text:
                    print("You said:", text)
                    return text
