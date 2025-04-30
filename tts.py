from gtts import gTTS
import os

def speak_kinyarwanda(text, output_path="outputs/response.mp3"):
    tts = gTTS(text=text, lang='rw')
    tts.save(output_path)
    os.system(f'start {output_path}')  # Use 'xdg-open' on Linux or 'afplay' on Mac
