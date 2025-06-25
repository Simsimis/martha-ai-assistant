# src/config.py
# --- The one and only configuration file for Martha ---

import os
from dotenv import load_dotenv

# This command searches for a .env file and loads its content
# into the environment, making them accessible to os.getenv()
load_dotenv()


# === API Keys (Now loaded securely from your .env file) ===
# This line will read the value of OPENAI_API_KEY from your .env file.
# If it's not found, it will return None.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")


# === Important Settings ===
WAKE_WORD = "martha"

# We will discover these values later with test_audio.py
AUDIO_INPUT_DEVICE_INDEX = None 
AUDIO_OUTPUT_DEVICE_INDEX = None 

# A flag to easily switch between modes
USE_ONLINE_MODE = True 


# --- Sanity Checks (Optional but recommended) ---
if not OPENAI_API_KEY:
    print("-----------------------------------------------------------------")
    print("WARNING: OPENAI_API_KEY is not set in your .env file.")
    print("The Online Mode will not work until you set the key.")
    print("-----------------------------------------------------------------")