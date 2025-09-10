from collections import Counter

emotion_keywords = {
    "happy": "joy",
    "joy": "joy",
    "smile": "joy",
    "laugh": "joy",
    "excited": "joy",
    "love": "joy",

    "sad": "sadness",
    "cry": "sadness",
    "lonely": "sadness",
    "depressed": "sadness",

    "angry": "anger",
    "mad": "anger",
    "furious": "anger",
    "annoyed": "anger",
    "hate": "anger",

    "afraid": "fear",
    "scared": "fear",
    "fear": "fear",
    "worried": "fear",
    "nervous": "fear",
    "anxious": "fear"
}

# Emoji mapping for emotions
emotion_emojis = {
    "joy": "🙂",
    "sadness": "😔",
    "anger": "😡",
    "fear": "😨"
}

def detect_emotion(text):
    words = text.lower().split()
    emotion_counts = Counter()

    for word in words:
        if word in emotion_keywords:
            emotion = emotion_keywords[word]
            emotion_counts[emotion] += 1

    if not emotion_counts:
        return None, "🤔 No clear emotion detected."

    dominant_emotion = emotion_counts.most_common(1)[0][0]
    emoji = emotion_emojis.get(dominant_emotion, "❓")
    return dominant_emotion, f"Detected Emotion: {dominant_emotion.capitalize()} {emoji}"

def main():
    print("👋 Welcome to the Emotion Detector!")
    print("Type a sentence to analyze (or 'exit' to quit).\n")

    while True:
        user_input = input("Enter your sentence: ").strip()
        if user_input.lower() == "exit":
            print("👋 Goodbye! Stay positive 💫")
            break

        _, message = detect_emotion(user_input)
        print(message, "\n")

if __name__ == "__main__":
    main()
