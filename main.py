from asr import transcribe
from nlp import match_question
from tts import speak_kinyarwanda
from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")
login(token=token)


audio_file = "data/audios/rw-test01.mp3"  # Replace with your test audio

# Step 1: Transcribe
question = transcribe(audio_file)
print("🔊 Question:", question)

# Step 2: Match answer
answer = match_question(question)
print("💬 Answer:", answer)

# Step 3: Speak the answer
speak_kinyarwanda(answer)
