# WhatsApp Audio Order

This repository contains a minimal, runnable pipeline that:

1. Takes an audio file
2. Transcribes it using Whisper
3. Cleans the transcription
4. Extracts a structured order
5. Outputs a confidence score

## Setup

## System Dependency

This project requires `ffmpeg` for audio decoding.

Verify installation:
```bash
ffmpeg -version


```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

