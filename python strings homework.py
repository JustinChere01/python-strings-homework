reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "This was a poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        if keyword in review.lower():
            review_with_highlight = review.replace(keyword, keyword.upper())
            print(review_with_highlight)


def tally_sentiment(review):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    count_positive = sum(review.lower().count(word) for word in positive_words)
    count_negative = sum(review.lower().count(word) for word in negative_words)

    return count_positive, count_negative

# Example reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Calculate sentiment for each review
for review in reviews:
    count_positive, count_negative = tally_sentiment(review)
    print(f"Review: {review}")
    print(f"Positive words: {count_positive}")
    print(f"Negative words: {count_negative}")

def create_summary(review):
    if len(review) <= 30:
        return review
    else:
        # Find the last space before the 30th character
        last_space = review.rfind(' ', 0, 30)
        if last_space != -1:
            return review[:last_space] + "…"
        else:
            # If no space found, simply truncate at 30 characters
            return review[:30] + "…"

# Example usage:
review_text = "This is a sample review that exceeds 30 characters. It should be summarized."
summary = create_summary(review_text)
print(summary)
