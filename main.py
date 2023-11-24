import pyaudio
import keyboard
import wave
import requests
import time
from deepl import DeepLCLI
from api_key import API_KEY_ASSEMBLYAI
import urllib.parse
import sounddevice as sd
import soundfile as sf

while True:
    # record voice from mic
    frame_per_buff = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    wave_output_filename = "recording.wav"

    p = pyaudio.PyAudio()

    stream = p.open(
        format=format,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=frame_per_buff,
    )

    frames = []

    print("Press 'v' to start recording...")
    while True:
        if keyboard.is_pressed("v"):
            # Disable the 'v' key
            keyboard.block_key("v")
            print("Recording...")
            while True:
                data = stream.read(frame_per_buff)
                frames.append(data)
                if not keyboard.is_pressed("v"):
                    # Unblock the 'v' key
                    keyboard.unblock_key("v")
                    break
            break

    print("Stopped recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(wave_output_filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))
    wf.close()

    # voice recognition !!

    upload_endpoint = "https://api.assemblyai.com/v2/upload"
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

    headers = {"authorization": API_KEY_ASSEMBLYAI}
    filename = "recording.wav"

    def upload(filename):
        def read_file(filename, chunk_size=5242880):
            with open(filename, "rb") as _file:
                while True:
                    data = _file.read(chunk_size)
                    if not data:
                        break
                    yield data

        upload_response = requests.post(
            upload_endpoint, headers=headers, data=read_file(filename)
        )

        audio_url = upload_response.json()["upload_url"]
        return audio_url

    def transcribe(audio_url):
        transcript_request = {"audio_url": audio_url}
        transcript_response = requests.post(
            transcript_endpoint, json=transcript_request, headers=headers
        )
        job_id = transcript_response.json()["id"]
        return job_id

    def pull(transcript_id):
        pulling_endpoint = transcript_endpoint + "/" + transcript_id
        pulling_response = requests.get(pulling_endpoint, headers=headers)
        return pulling_response.json()

    def get_transcription_result_url(audio_url):
        transcript_id = transcribe(audio_url)
        while True:
            data = pull(transcript_id)
            if data["status"] == "completed":
                return data, None
            elif data["status"] == "error":
                return data, data["error"]

    # save transcript
    def save_transcription(audio_url):
        data, error = get_transcription_result_url(audio_url)

        if data:
            text_filename = filename + ".txt"
            with open(text_filename, "w") as f:
                f.write(data["text"])
            print("transcription saved!")
        elif error:
            print("error!", error)

    audio_url = upload(filename)
    save_transcription(audio_url)

    # translate !!

    # open the file for reading
    with open("recording.wav.txt", "r") as file:
        # read the contents of the file
        contents = file.read()

    # print the contents of the file
    print("you said: ", contents)

    deepl = DeepLCLI("en", "ja")
    translate = deepl.translate(contents)
    print("Translate to JP: ", translate)

    # TTS !!
    text = translate
    voicevox_url = "http://localhost:50021"
    # You can change the voice to your liking. You can find the list of voices on speaker.json
    # or check the website https://voicevox.hiroshiba.jp
    params_encoded = urllib.parse.urlencode({"text": text, "speaker": 46})
    request = requests.post(f"{voicevox_url}/audio_query?{params_encoded}")
    params_encoded = urllib.parse.urlencode(
        {"speaker": 46, "enable_interrogative_upspeak": True}
    )
    request = requests.post(
        f"{voicevox_url}/synthesis?{params_encoded}", json=request.json()
    )

    with open("JP_Voice.wav", "wb") as outfile:
        outfile.write(request.content)
        outfile.close

    data, fs = sf.read("JP_Voice.wav", dtype="float32")
    sd.play(data, fs)
    status = sd.wait()

    time.sleep(1)
