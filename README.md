# 🎤 Python Speech-to-Speech Voice Assistant

A simple yet powerful voice assistant built with Python that can listen to voice commands, process them, and respond with speech.

## Features

✨ **Core Features:**
- 🎙️ Speech Recognition - Convert voice to text using Google Speech API
- 🔊 Text-to-Speech - Respond with natural-sounding speech
- ⏰ Time & Date - Ask for current time and date
- 👋 Greetings - Respond to hello/hi commands
- 🎯 Extensible - Easy to add custom commands
- 📝 Command Logging - Keep track of all voice commands

## Requirements

- Python 3.7+
- Microphone (for input)
- Speaker (for output)
- Internet connection (for Google Speech API)

## Installation

1. **Clone the repository:**
```bash
git clone git@github.com:adithyan916/BUDDY.git
cd BUDDY
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install system dependencies (Linux/Ubuntu):**
```bash
sudo apt-get install python3-dev portaudio19-dev
```

4. **For macOS:**
```bash
brew install portaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```

## Usage

Run the voice assistant:
```bash
python voice_assistant.py
```

## Available Commands

| Command | Response |
|---------|----------|
| "What's the time?" | Tells current time |
| "What's the date?" | Tells current date |
| "Hello" / "Hi" | Greets you |
| "Exit" / "Quit" | Stops the assistant |

## Configuration

Edit `config.py` to customize:
- Speech rate (50-300 words per minute)
- Volume level (0.0-1.0)
- Voice gender (male/female)
- Timeout settings

## Troubleshooting

**Microphone not detected:**
- Check microphone permissions
- Test with: `python -m speech_recognition`

**PyAudio installation issues:**
- Windows: Use pre-built wheels
- macOS: Install via Homebrew first
- Linux: Install portaudio dev files

**No internet connection:**
- Google Speech API requires internet
- Consider using offline solutions (Sphinx, PocketSphinx)

## Future Enhancements

- [ ] Weather API integration
- [ ] Calendar integration
- [ ] Email reading
- [ ] Voice command customization
- [ ] Multiple language support
- [ ] Offline speech recognition

## License

MIT License - feel free to use and modify!

## Support

For issues or questions, create an issue on GitHub.
