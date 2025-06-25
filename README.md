# Martha AI Assistant

Martha is a DIY, voice-first AI home assistant with a unique personality—think Karen from SpongeBob, but smarter and snarkier. Built inside a retro monitor and powered by a Raspberry Pi 4, Martha is designed to be your witty, always-on digital companion. She listens, she talks, she might roast you, but she always helps.

---

## Features

- **Wake Word Detection:** Hands-free activation with "Hey Martha" (using Porcupine or similar).
- **Speech-to-Text & Text-to-Speech:** Supports both cloud (OpenAI Whisper, Google TTS, ElevenLabs) and local (offline) modes.
- **AI Brain:** Online (GPT-4/Gemini) and offline (Llama) LLM support for flexible, robust responses.
- **Distinct Personality:** Sarcastic, witty, and helpful—Martha never breaks character.
- **Modular Hardware Integration:** Audio via ReSpeaker 2-Mics Pi HAT, vision via USB webcam, display via HDMI monitor.
- **Customizable & Extensible:** Easily add new skills, smart home integrations, or personality tweaks.

---

## Hardware
- **Brain:** Raspberry Pi 4 (8GB RAM recommended)
- **Audio:** ReSpeaker 2-Mics Pi HAT (input/output)
- **Vision:** USB Webcam
- **Display:** HDMI Monitor (preferably retro)

---

## Software Architecture
- **Online Mode:** Uses cloud APIs for best performance (OpenAI, Google, ElevenLabs).
- **Offline Mode:** Runs local models for privacy and resilience.
- **Personality Engine:** System prompts and responses crafted for maximum snark and utility.
- **Visualization:** Animated oscilloscope/sine wave face using `pygame`.

---

## Getting Started
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/martha-ai-assistant.git
   cd martha-ai-assistant
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure your API keys:**
   - Edit `src/config.py` and add your OpenAI, Google, and ElevenLabs API keys.
4. **Connect your hardware:**
   - Attach the ReSpeaker HAT, webcam, and monitor to your Raspberry Pi.
5. **Run Martha:**
   ```sh
   python src/main.py
   ```

For detailed setup, see [docs/setup_guide.md](docs/setup_guide.md).

---

## Example Conversation
> **You:** Hey Martha, what's the weather?
>
> **Martha:** Oh, you couldn't just look outside? Fine. It's 22°C and sunny. You're welcome.

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. Help Martha become even more sarcastic, smart, and useful.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Martha AI Assistant** — She might enjoy you back. Or not.