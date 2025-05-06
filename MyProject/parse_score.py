import json

def load_score(file_path):
    with open(file_path, encoding='utf-8') as f:
        score = json.load(f)
    return score

def parse_to_diffSinger_input(score_json):
    notes = []
    pitch = []
    durations = []
    phonemes = []

    for note in score_json:
        notes.append(note["note"])
        durations.append(note["duration"])
        pitch.append((note["start"], note["note"])) 
        phonemes.append(" ".join(note["phonemes"]))

    print("Notes:", notes)
    print("Durations:", durations)
    print("Phonemes per syllable:", phonemes)

    return {
        "notes": notes,
        "durations": durations,
        "pitch_map": pitch,
        "phonemes": phonemes
    }

if __name__ == "__main__":
    score = load_score("score.json")
    parsed = parse_to_diffSinger_input(score)

