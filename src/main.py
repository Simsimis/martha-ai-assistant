from src.core.assistant import handle_input
from src.hardware.audio import listen, speak  # Υποθέτουμε ότι έχεις υλοποιήσει listen()

def main():
    print("Η Μάρθα είναι έτοιμη! Μίλα της...")
    while True:
        # Ακούει τον χρήστη (θα υλοποιήσεις το listen με Whisper.cpp)
        user_input = listen()  
        
        if user_input.lower() == "στόπ":
            break
            
        # Επεξεργασία και απάντηση
        response = handle_input(user_input)
        print(f"Μάρθα: {response}")
        speak(response)

if __name__ == "__main__":
    main()