# src/hardware/audio.py
# This module will contain the AudioHandler class, responsible for all
# audio interactions, including recording from the ReSpeaker and playing audio.

import pyaudio
import wave
import time
from src import config  # Import our configuration

class AudioHandler:
    """Handles all audio input and output operations."""

    def __init__(self):
        """
        Initializes the PyAudio instance and gets device indices from the config.
        """
        self.p = pyaudio.PyAudio()
        self.input_device_index = config.AUDIO_INPUT_DEVICE_INDEX
        self.output_device_index = config.AUDIO_OUTPUT_DEVICE_INDEX
        
        # Audio stream parameters
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000  # 16kHz is standard for voice recognition
        self.CHUNK = 1024
        
        print("AudioHandler initialized.")
        if self.input_device_index is None:
            print("  - Input device index is not set. Recording will use default device.")
        else:
            print(f"  - Using input device index: {self.input_device_index}")

    def __del__(self):
        """
        Ensures that the PyAudio instance is terminated when the object is deleted.
        """
        print("Terminating PyAudio instance.")
        self.p.terminate()

    # --- We will add more methods here, like record() and play(), in the next steps ---
    def record_audio(self, duration=5, output_filename="command.wav"):
        """Records audio from the input device for a specified duration."""
        
        if self.input_device_index is None:
            print("ERROR: No input device index is set. Cannot record.")
            return False

        print(f"\n* Preparing to record for {duration} seconds...")
        
        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK,
                             input_device_index=self.input_device_index)

        print("* Recording...")
        
        frames = []
        for _ in range(0, int(self.RATE / self.CHUNK * duration)):
            data = stream.read(self.CHUNK)
            frames.append(data)
            
        print("* Finished recording.")

        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        # Save the recorded data as a WAV file
        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
        
        print(f"* Audio saved to {output_filename}")
        return True

    def speak(self, text):
        """
        Speaks the given text using the pyttsx3 library (offline and free).
        """
        try:
            # Lazy import pyttsx3 only when needed
            import pyttsx3
            engine = pyttsx3.init()
            print(f"\nMartha says: '{text}'")
            engine.say(text)
            engine.runAndWait()
            return True
        except Exception as e:
            print(f"An error occurred in pyttsx3: {e}")
            return False

# This part is just for testing if this file works on its own
if __name__ == '__main__':
    print("Running a test of the AudioHandler...")
    handler = AudioHandler()
    # === NEW TEST CODE for FREE SPEECH ===
    handler.speak("Hello, World! I can speak, and it costs nothing! Ha ha ha.")
    handler.speak("Αυτό είναι το δεύτερο τεστ, στα Ελληνικά!")
    # ======================================
    del handler