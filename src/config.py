# src/config.py
# --- The one and only configuration file for Martha ---

# No API keys needed for offline mode!

# === Important Settings ===
WAKE_WORD = "martha"

# We will discover these values later with test_audio.py
AUDIO_INPUT_DEVICE_INDEX = 1 
AUDIO_OUTPUT_DEVICE_INDEX = 4

# A flag to easily switch between modes
USE_ONLINE_MODE = False