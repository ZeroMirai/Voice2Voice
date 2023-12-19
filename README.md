# Voice2Voice

Voice2Voice is a voice-to-voice translator designed to break language barriers. It can convert your speech to Japanese and play it back using the VoiceVox to generate text-to-speech. Additionally, it utilizes the Assemble AI API for speech-to-text conversion and the fast Google Translate API for translation. This project is useful for people who want to communicate in Japanese without the need for typing or reading.

---
## Table of Contents

- [Voice2Voice](#voice2voice)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [File Structure](#file-structure)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Contributing](#contributing)
    - [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
    - [Pull Requests](#pull-requests)
  - [Note](#note)
  - [License](#license)
  - [Credits](#credits)

## Features

- **Convert speech in realtime**
- **45+ TTS Models from VoiceVox Engine**

## Prerequisites

- **Python** Version 3.11. Download it [here](https://www.python.org/downloads/).
- **Voicevox software** Version 0.14.7 or higher. Download it [here](https://voicevox.hiroshiba.jp/), installed and running.
- **API keys** From AssemblyAI, you can get it from [here](https://www.assemblyai.com/app/account).

## Installation

Follow these steps to install and set up Voice2Voice.

1. Download the project zip file from GitHub or Clone this repository by typing these in terminal or command prompt (but if you choose to download the project as a zip file you'll also need to extract the zip file).
   ```
   git clone https://github.com/ZeroMirai/Voice2Voice.git
   ```
2. Open a terminal or command prompt and change the directory to the project folder by typing `cd` followed by where this folder is located for example `cd C:\Git_hub\Voice2Voice`.
3. Install all necessary library by typing.
   ```
   pip install -r requirements.txt
   ```
4. Configure the necessary API keys and other config in `config.txt`.
## File Structure

- 📁`functions`: Contains modular components of the project.
   - 📝`record_voice.py`: Voice recording function.
   - 📝`utilis.py`: Utilities for all script.
   - 📝`voice_recognition.py`: Implements speech-to-text using the AssemblyAI API.
- 📁`temp`: Store various temporary file.
- 📝`utilis.py`: Main script for executing the Voice2Voice program.
- 📝`config.txt`: this file stores TTS model and AssembleAI API configurations.

## Configuration

Before running the program, Ensure you have changed all the configurations and **pasted them right after the : in the file**. The file must have the following format.
  ```
  assembly_api_key:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  voice_vox_text_to_speech_model:xx
  ```
- Edit the config.txt file with your prefering TTS model (you can compare `speaker.json` name with [VoiceVox](https://voicevox.hiroshiba.jp/) and type id number you desire.) and for assembly_api_key copy and paste your AssemblyAI API key here but if you didn't have it, you can get it [here](https://www.assemblyai.com/app/account).
  
## Usage

To use Voice2Voice with Discord and Games, you can follow this guide in [How to use with Discord and Games](how_to_use_with_discord_and_games.md). For normal usage in the terminal or command prompt, you can follow the guide below.
1. Open VoiceVox engine.
2. Open `run.bat`.
3. Follow on-screen prompts and interact with Voice2Voice.

---
## Contributing

Voice2Voice is a project created for fun, if you are interested to contribute in this project here is how you can make this project better for everyone.

### Bug Reports and Feature Requests

If you found a bug or have an idea for a new feature, feel free to requests and reports by [open an issue](https://github.com/ZeroMirai/Voice2Voice/issues) on GitHub and post it if it's a bug please give as much detail as possible or suggest an idea please include a step or a clear description.

### Pull Requests

If you have suggestions or improvements.

1. Fork the repository and create your own branch from `main`.
2. Work on your changes.
3. Write clear, concise commit messages that describe the purpose of your changes.
4. Open a pull request and provide a detailed description of your changes.

I'm primarily looking for code improvements and bug fixes. Once your changes are approved, they will be merged into the main project.

### ⭐ Share and Give a Star ⭐

**If you find this project useful I would be really grateful if you could consider sharing this small project with others and giving it a star on GitHub.**

---

## Note

- Ensure that you have the required dependencies and configuration set up before running the code.
- Running the program and VoiceVox engine simultaneously is necessary for proper program functionality.
- If you use this program with discord_and_games, you need to redo steps 5-8 every time the program is opened.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- **Voicevox by Hiroshiba** - Used to synthesize speech in Japanese. For more information, visit [VoiceVox](https://voicevox.hiroshiba.jp/)
- **Googletrans** - Used to translate text to Japanese. For more information, visit [Googletrans](https://github.com/ssut/py-googletrans)
- **AssemblyAI API** - Used to convert speech to text. For more information, visit [AssemblyAI API](https://www.assemblyai.com/)
