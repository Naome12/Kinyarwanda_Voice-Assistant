import gradio as gr
from asr import transcribe_audio
from nlp import get_best_match
from tts import speak

def assistant(audio):
    text = transcribe_audio(audio)
    response = get_best_match(text, qa)
    speak(response)
    return text, response

gr.Interface(fn=assistant, 
             inputs=gr.Audio(source="microphone", type="filepath"),
             outputs=["text", "text"]).launch()
