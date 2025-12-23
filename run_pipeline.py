from pipeline.transcribe import transcribe_audio
from pipeline.clean_text import clean_transcription
from pipeline.extract_order import extract_order
from pipeline.confidence import confidence_score
import json

AUDIO_FILE = "audio_samples/sample_order.wav"

def main():
    raw_text = transcribe_audio(AUDIO_FILE)
    clean_text = clean_transcription(raw_text)
    order = extract_order(clean_text)
    confidence = confidence_score(clean_text, order)

    output = {
        "transcription": raw_text,
        "cleaned_text": clean_text,
        "order": order.model_dump(),
        "confidence": confidence,
    }

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
