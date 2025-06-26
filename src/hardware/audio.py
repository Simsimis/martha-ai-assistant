import subprocess
import os
from pathlib import Path

# --- Configuration ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PIPER_EXE_PATH = PROJECT_ROOT / "vendor" / "piper" / "piper.exe"
MODEL_PATH = PROJECT_ROOT / "vendor" / "piper" / "el_GR-rapunzelina-low.onnx"
OUTPUT_WAV_PATH = PROJECT_ROOT / "output.wav"

def speak(text_to_speak: str):
    """
    Μετατρέπει ένα κείμενο σε ομιλία χρησιμοποιώντας το piper.exe και το αναπαράγει.
    """
    if not PIPER_EXE_PATH.exists():
        print(f"Σφάλμα: Το αρχείο piper.exe δεν βρέθηκε στο {PIPER_EXE_PATH}")
        return

    if not MODEL_PATH.exists():
        print(f"Σφάλμα: Το μοντέλο φωνής .onnx δεν βρέθηκε στο {MODEL_PATH}")
        return

    print(f"Παρασκευάζεται ομιλία για το κείμενο: '{text_to_speak}'...")

    command = [
        str(PIPER_EXE_PATH),
        "--model", str(MODEL_PATH),
        "--output_file", str(OUTPUT_WAV_PATH),
    ]

    try:
        # Τρέχουμε το piper.exe, περνώντας το κείμενο ως είσοδο (input)
        # Αυτή είναι η σωστή μέθοδος που λύνει το πρόβλημα!
        subprocess.run(
            command,
            input=text_to_speak,
            encoding="utf-8",
            check=True,
            capture_output=True,
            text=True
        )

        print("Η ομιλία δημιουργήθηκε. Ξεκινά η αναπαραγωγή...")

        # Χρησιμοποιούμε το playsound που ήδη εγκαταστήσαμε
        from playsound import playsound
        playsound(str(OUTPUT_WAV_PATH))
        
        print("Η αναπαραγωγή ολοκληρώθηκε.")

    except FileNotFoundError:
        print(f"Σφάλμα: Δεν ήταν δυνατή η εκτέλεση του {PIPER_EXE_PATH}.")
    except subprocess.CalledProcessError as e:
        print(f"Σφάλμα κατά την εκτέλεση του Piper: {e}")
        print(f"Error output:\n{e.stderr}")
    except Exception as e:
        print(f"Προέκυψε ένα απρόσμενο σφάλμα: {e}")
    finally:
        if os.path.exists(OUTPUT_WAV_PATH):
            os.remove(OUTPUT_WAV_PATH)

if __name__ == "__main__":
    speak("Επιτέλους. Αυτό πήρε περισσότερο από όσο έπρεπε. Ας ελπίσουμε ότι τώρα με ακούς.")