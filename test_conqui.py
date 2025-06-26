import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from TTS.api import TTS

# --- Configuration ---
# 👈 Καλούμε απευθείας το πλήρες "πακέτο" μοντέλου.
# Το Coqui θα καταλάβει αυτόματα ποιο μοντέλο γλώσσας και ποιον vocoder να χρησιμοποιήσει.
MODEL_PACKAGE = "tts_models/el/cv/vits"

try:
    print(f"Αρχικοποίηση του Coqui TTS με το πλήρες πακέτο: {MODEL_PACKAGE}")
    print("\nΠαρακαλώ περιμένετε, το μοντέλο φορτώνεται...")

    # Αρχικοποίηση του TTS με το ένα, σωστό όνομα.
    tts = TTS(MODEL_PACKAGE, progress_bar=True)

    print("\nΤο μοντέλο φορτώθηκε με επιτυχία!")
    
    text_to_speak = "Ας δοκιμάσουμε ξανά. Με τον σωστό κώδικα, η ποιότητα της φωνής μου πρέπει να είναι η καλύτερη δυνατή."
    output_file = "coqui_final_test.wav"
    
    print(f"\nΔημιουργείται αρχείο ήχου για το κείμενο: '{text_to_speak}'")
    
    # Δημιουργία του αρχείου ήχου
    tts.tts_to_file(text=text_to_speak, file_path=output_file)
    
    print("\n---------------------------------------------------------")
    print(f"!!! ΕΠΙΤΥΧΙΑ !!!")
    print(f"Το αρχείο ήχου '{output_file}' δημιουργήθηκε.")
    print("Παρακαλώ, ακούστε το και πείτε μου τη γνώμη σας.")
    print("---------------------------------------------------------")

except Exception as e:
    print(f"\nΠΡΟΕΚΥΨΕ ΣΦΑΛΜΑ: {e}")