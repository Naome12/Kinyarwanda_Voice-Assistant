# 🗣️ Kinyarwanda Voice Assistant (ASR + TTS)

This project is a simple voice assistant that listens to `.wav` audio recordings in **Kinyarwanda**, transcribes them using a **Whisper ASR model**, finds a matching response, and replies using a **VITS text-to-speech model**.

---

## 🔧 Features

- 🎙️ Transcribes spoken Kinyarwanda using [`mbazaNLP/Whisper-Small-Kinyarwanda`](https://huggingface.co/mbazaNLP/Whisper-Small-Kinyarwanda)
- 🗣️ Responds with natural Kinyarwanda speech using [`facebook/mms-tts-kin`](https://huggingface.co/facebook/mms-tts-kin)
- ✅ Matches predefined questions and answers
- 📁 Saves and plays generated responses

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Naome12/Kinyarwanda_Voice-Assistant.git
cd Kinyarwanda_Voice-Assistant


## 📦 2. Install Dependencies

Make sure you are using **Python 3.8+**, then install the required packages:

```bash
pip install torch torchaudio transformers soundfile
```

---

## 🖥️ FFmpeg Setup (Windows Only)

To enable audio playback from the script, FFmpeg must be installed.

### 🔽 Steps to Install:

1. Download FFmpeg from [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds)
2. Extract the ZIP file
3. Locate the `bin` folder inside the extracted directory

### ⚙️ Choose One of the Following:

**Option A — Add to System Environment Variables:**

- Open "Environment Variables"
- Add the full path to `ffmpeg\bin` to your system `PATH`

**Option B — Modify the Script Directly:**

In your Python script (`main.py`), add:

```python
os.environ["PATH"] += os.pathsep + r"C:\path\to\ffmpeg\bin"
```

---

## 🧠 Pretrained Models

These models are automatically downloaded from Hugging Face when you run the script for the first time:

| Task                | Model Name                            |
|---------------------|----------------------------------------|
| ASR (Transcription) | `mbazaNLP/Whisper-Small-Kinyarwanda`   |
| TTS (Speech)        | `facebook/mms-tts-kin`                 |

---

## 📂 Project Structure

```plaintext
kinyarwanda-voice-assistant/
│
├── data/
│   ├── audio/              # Input .wav audio files
│   └── outputs/            # Output audio responses (auto-created)
│
├── main.py                 # Main script (edit as needed)
└── README.md               # This file
```

---

## ▶️ Running the Project

1. Place your `.wav` files in the `data/audio/` directory
2. Run the script:

```bash
python main.py
```

Each `.wav` file will be:

- 🧠 Transcribed from speech to text
- ❓ Matched with a known question
- 🔊 Replied to with synthesized speech
- 💾 Saved to `data/outputs/` and played automatically (on Windows)

---

## 💬 Supported Questions

Below are the default questions the assistant understands and replies to:

| Question                          | Response                                |
|-----------------------------------|------------------------------------------|
| `amakuru`                         | Ni meza, urakoze!                        |
| `witwa nde`                       | Nitwa Tuyishime                          |
| `bite byawe`                      | Ni byiza!                                |
| `umurwa mukuru w'u Rwanda`        | Umurwa mukuru w'u Rwanda ni Kigali.      |
| `umuyobozi w'u Rwanda ninde`      | Umuyobozi w'u Rwanda ni Paul Kagame!     |

🛠️ To add more questions and answers, simply update the `qa_pairs` dictionary in `main.py`.

---

## 📌 Notes

- Make sure your audio files are **mono `.wav`** and **sampled near 16kHz**
- Works best with **clearly spoken input**
- Playback uses `os.system("start ...")`, which is **Windows-specific** — you can modify it for Linux/macOS

---
