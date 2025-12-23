import regex as re

NUMBER_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "free": "3"  # <-- intentional ASR correction
}

def clean_transcription(text: str) -> str:
    text = text.lower()

    for word, digit in NUMBER_WORDS.items():
        text = text.replace(word, digit)

    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
