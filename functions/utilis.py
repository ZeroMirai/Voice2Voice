import soundfile as sf
import sounddevice as sd
import requests
import romajitable
import urllib
from googletrans import Translator

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        output = file.read()
    return output

# Function to save a text from parameter and save it to .txt file
def save_text_to_file(unsaved_text, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(unsaved_text)

# Function to read config file and return it
def read_config(config_file_path):
    with open(config_file_path, "r") as config_file:
        for line in config_file:
            line = line.strip()
            if line.startswith("assembly_api_key:"):
                assembly_key = line[17:]
            elif line.startswith("voice_vox_text_to_speech_model:"):
                voice_vox_text_to_speech_model = line[31:]
                
    return assembly_key, voice_vox_text_to_speech_model

# Function to translate text
def translate(untranslated):
    print("Input: ", untranslated)
    translator = Translator()
    result = translator.translate(untranslated, dest='ja')
    translated_text = result.text
    print(f"Translated: {translated_text} \n---------------------------------")
    return translated_text
    
    
# Function to create a text-to-speech file using voicevox engine
def generate_voicevox_text_to_speech_file(jp_text, voice_vox_text_to_speech_model, output_filename):
    # Turn some of the input that have a english text to katakana text for example
    # If input contain a word "apple" it'll turn it to "appuru"
    result = romajitable.to_kana(jp_text)
    katakaned = result.katakana

    # Text-to-speech part (make sure you have open VOICEVOX.exe)
    voicevox_url = "http://localhost:50021"
    params_encoded = urllib.parse.urlencode(
        {"text": katakaned, "speaker": voice_vox_text_to_speech_model}
    )
    request = requests.post(f"{voicevox_url}/audio_query?{params_encoded}")
    params_encoded = urllib.parse.urlencode(
        {
            "speaker": voice_vox_text_to_speech_model,
            "enable_interrogative_upspeak": True,
        }
    )
    request = requests.post(
        f"{voicevox_url}/synthesis?{params_encoded}", json=request.json()
    )

    with open(output_filename, "wb") as outfile:
        outfile.write(request.content)
        outfile.close()
   
# Function to play a generated text-to-speech file
def play_audio_file(file_name):
    try:
        data, fs = sf.read(file_name, dtype="float32")
        sd.play(data, fs)
        status = sd.wait()
    except sd.PortAudioError as e:
        print(f"An error occurred while trying to play the audio: {e}")
        
# Function to test if VoiceVox is opend
def run_test(
    VOICE_VOX_TEXT_TO_SPEECH_MODEL,
    output_filename
):
    generate_voicevox_text_to_speech_file("操作する準備ができています", VOICE_VOX_TEXT_TO_SPEECH_MODEL, output_filename)
    play_audio_file(output_filename)