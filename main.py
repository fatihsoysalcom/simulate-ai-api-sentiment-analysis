import json

def simulate_ai_sentiment_api(text: str) -> dict:
    """
    Simulates a call to an AI API for sentiment analysis.
    This function acts as a 'bridge' to a pre-trained AI model,
    as described in the article. Developers don't need to build
    the sentiment logic from scratch; they just call the API.
    """
    text_lower = text.lower()
    
    # Define keywords for sentiment detection (simplified AI model)
    positive_keywords = ["harika", "mükemmel", "iyi", "başarılı", "sevdim", "güzel", "olumlu", "beğendim"]
    negative_keywords = ["kötü", "berbat", "olumsuz", "sevmedim", "hayal kırıklığı", "sorunlu", "beğenmedim"]
    
    positive_score = sum(text_lower.count(kw) for kw in positive_keywords)
    negative_score = sum(text_lower.count(kw) for kw in negative_keywords)
    
    sentiment = "neutral"
    confidence = 0.5 # Default confidence
    
    if positive_score > negative_score:
        sentiment = "positive"
        # Confidence increases with the difference in scores
        confidence = min(1.0, 0.5 + (positive_score - negative_score) * 0.15)
    elif negative_score > positive_score:
        sentiment = "negative"
        confidence = min(1.0, 0.5 + (negative_score - positive_score) * 0.15)
    else:
        # If scores are equal or zero, it's neutral, but adjust confidence if keywords were found
        if positive_score > 0 or negative_score > 0:
            confidence = 0.6 # Slightly more confident than default if keywords are present but balanced
        
    return {
        "input_text": text,
        "sentiment": sentiment,
        "confidence": round(confidence, 2),
        "model_version": "v1.0-simulated-sentiment"
    }

if __name__ == "__main__":
    print("--- Simulating AI API Calls for Sentiment Analysis ---")
    print("This example demonstrates how applications can integrate AI capabilities")
    print("by making simple 'API calls' to pre-trained models, as discussed in the article.\n")

    # Example 1: Positive text
    text1 = "Bu ürün gerçekten harika, çok beğendim ve performansı mükemmel!"
    print(f"Analyzing: '{text1}'")
    result1 = simulate_ai_sentiment_api(text1)
    print(f"API Response: {json.dumps(result1, indent=2)}\n")

    # Example 2: Negative text
    text2 = "Hizmet çok kötüydü, tam bir hayal kırıklığı yaşadım."
    print(f"Analyzing: '{text2}'")
    result2 = simulate_ai_sentiment_api(text2)
    print(f"API Response: {json.dumps(result2, indent=2)}\n")

    # Example 3: Neutral/Mixed text
    text3 = "Ürün fena değil ama kargo biraz geç geldi."
    print(f"Analyzing: '{text3}'")
    result3 = simulate_ai_sentiment_api(text3)
    print(f"API Response: {json.dumps(result3, indent=2)}\n")
    
    # Example 4: Another positive
    text4 = "Bu makale çok başarılı ve açıklayıcıydı, okumaya değer."
    print(f"Analyzing: '{text4}'")
    result4 = simulate_ai_sentiment_api(text4)
    print(f"API Response: {json.dumps(result4, indent=2)}\n")

    print("--- End of Simulation ---")
