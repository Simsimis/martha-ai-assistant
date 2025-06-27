import sounddevice as sd
from piper import PiperVoice

# Φόρτωση μοντέλου
voice = PiperVoice.load("models/el_GR-rapunzelina-low.onnx")

def speak(text: str):
    # Βελτιωμένη φυσική ομιλία
    audio = voice.synthesize(
        text,
        length_scale=1.1,   # Ελαφρώς πιο αργό για φυσικότητα
        noise_scale=0.3,    # Λιγότερο "μηχανικό"
        noise_w=0.2         # Πιο σταθερή απόδοση
    )
    sd.play(audio, samplerate=voice.config.sample_rate)
    sd.wait()

def listen():
    # Stub: Επιστρέφει κείμενο για δοκιμή
    return input("Εσύ: ")