NEGATIVE_WORDS = [
    "poor", "bad", "worst", "waste", "not good","not respond", "terrible", "boring",
    "slow", "hard", "difficult", "disappointed", "dirty", "confusing",
    "useless", "frustrating", "annoying", "unhelpful", "ineffective",
    "unorganized", "irrelevant", "incomplete", "unclear", "stressful",
    "outdated", "weak", "poorly", "disappointing", "complicated",
    "lengthy", "unfair", "rude", "careless", "unprofessional",
    "inaccurate", "problematic", "tedious", "unsatisfactory"
]

POSITIVE_WORDS = [
    "clear", "clearly", "good", "excellent", "great", "awesome",
    "perfect", "nice", "satisfied", "best", "happy", "amazing",
    "fantastic", "outstanding", "wonderful", "helpful", "informative",
    "interesting", "effective", "supportive", "friendly",
    "interactive", "engaging", "brilliant", "impressive",
    "valuable", "motivating", "enjoyable", "comfortable",
    "professional", "knowledgeable", "organized",
    "responsive", "appreciated", "successful"
]

NEUTRAL_WORDS = [
    "okay", "average", "fine", "normal", "medium", "maybe",
    "not bad", "so so", "as usual", "acceptable", "moderate",
    "ordinary", "fair", "reasonable", "standard", "general",
    "typical", "balanced", "adequate", "consistent", "regular",
    "expected", "usual", "satisfactory", "neither", "mixed",
    "partially", "somewhat", "occasionally", "depends",
    "uncertain", "basic", "common"
]

print("=== Student Feedback Sentiment Predictor ===")
print("Type 'exit' to quit")

while True:

    feedback = input("\nEnter Feedback: ").strip().lower()

    if feedback == "exit":
        print("Goodbye!")
        break

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    # Count Positive Words
    for word in POSITIVE_WORDS:
        if word in feedback:
            positive_count += 1

    # Count Negative Words
    for word in NEGATIVE_WORDS:
        if word in feedback:
            negative_count += 1

    # Count Neutral Words
    for word in NEUTRAL_WORDS:
        if word in feedback:
            neutral_count += 1

    # Decision Logic
    if positive_count > negative_count and positive_count > neutral_count:
        sentiment = "Positive"

    elif negative_count > positive_count and negative_count > neutral_count:
        sentiment = "Negative"

    elif neutral_count > positive_count and neutral_count > negative_count:
        sentiment = "Neutral"

    elif positive_count > 0 and negative_count == 0:
        sentiment = "Positive"

    elif negative_count > 0 and positive_count == 0:
        sentiment = "Negative"

    elif neutral_count > 0 and positive_count == 0 and negative_count == 0:
        sentiment = "Neutral"

    else:
        sentiment = "Neutral"

    print("Predicted Sentiment:", sentiment)