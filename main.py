import os
from functions.record_voice import record_voice
from functions.utilis import translate, read_file, play_audio_file, generate_voicevox_text_to_speech_file, read_config, run_test
from functions.voice_recognition import voice_recognition

# File path
directory_path = os.path.dirname(os.path.realpath(__file__))
recognized_file = directory_path + r"\temp\recording.wav.txt"
recording_file = directory_path + r"\temp\recording.wav"
translated_voice_file = directory_path + r"\temp\translated.wav"
config_file = directory_path + r"\config.txt"

# Read every config and store it as constant
ASSEMBLY_KEY, VOICE_VOX_TEXT_TO_SPEECH_MODEL = read_config(config_file)

# Use run_test function to check if VoiceVox engine is open
run_test(VOICE_VOX_TEXT_TO_SPEECH_MODEL, translated_voice_file)

while True:
    record_voice(recording_file)
    voice_recognition(ASSEMBLY_KEY, recording_file)
    untranslated_text = read_file(recognized_file)
    translated_text = translate(untranslated_text)
    generate_voicevox_text_to_speech_file(translated_text, VOICE_VOX_TEXT_TO_SPEECH_MODEL, translated_voice_file)
    play_audio_file(translated_voice_file)