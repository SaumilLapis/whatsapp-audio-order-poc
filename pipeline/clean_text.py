import regex as re

NUMBER_NORMALIZATION = {
    "one": "1",
    "two": "2",
    "three": "3",
    "free": "3",
    "four": "4",
    "five": "5",
}

def clean_transcription(text: str) -> str:
    text = text.lower()

    for word, digit in NUMBER_NORMALIZATION.items():
        text = text.replace(word, digit)

    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text
