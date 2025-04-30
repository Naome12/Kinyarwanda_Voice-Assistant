import torchaudio
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Load .env

# Load the model and processor
model = WhisperForConditionalGeneration.from_pretrained("benax-rw/KinyaWhisper")
processor = WhisperProcessor.from_pretrained("benax-rw/KinyaWhisper")

def transcribe(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)

    # Convert to mono if needed
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    inputs = processor(waveform.squeeze(), sampling_rate=sample_rate, return_tensors="pt")
    predicted_ids = model.generate(inputs["input_features"])
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription
