import shutil
import sys
import json

from pipeline.transcribe import transcribe_audio
from pipeline.clean_text import clean_transcription
from pipeline.extract_order import extract_order
from pipeline.confidence import compute_confidence

if not shutil.which("ffmpeg"):
    print("ERROR: ffmpeg not found. Please install ffmpeg.")
    sys.exit(1)

AUDIO_FILE = "audio_samples/sample_order.wav"

def main():
    raw_text = transcribe_audio(AUDIO_FILE)
    clean_text = clean_transcription(raw_text)
    order = extract_order(clean_text)

    confidence_data = compute_confidence(raw_text, clean_text, order)

    output = {
        "transcription": raw_text,
        "cleaned_text": clean_text,
        "order": order.model_dump(),
        **confidence_data,
    }

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
