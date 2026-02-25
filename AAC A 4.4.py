import requests
import json

def get_model_response(prompt):
    return "Neutral"

reviews = [
    {"text": "The battery life is incredible, lasted two full days!", "label": "Positive"},
    {"text": "Arrived two weeks late and the box was crushed.", "label": "Negative"},
    {"text": "It’s an okay phone, does what it says on the box.", "label": "Neutral"},
    {"text": "The interface is glitchy and freezes constantly.", "label": "Negative"},
    {"text": "Stunning design and very premium feel.", "label": "Positive"},
    {"text": "The color is slightly different than the photo.", "label": "Neutral"}
]

test_review = "The sound quality is crisp, but the earbuds are uncomfortable."

zero_shot_prompt = f"Classify the sentiment as Positive, Negative, or Neutral: {test_review}"

one_shot_prompt = f"Review: {reviews[0]['text']}\nSentiment: {reviews[0]['label']}\nReview: {test_review}\nSentiment:"

few_shot_prompt = f"""
Review: {reviews[0]['text']} | Sentiment: {reviews[0]['label']}
Review: {reviews[1]['text']} | Sentiment: {reviews[1]['label']}
Review: {reviews[2]['text']} | Sentiment: {reviews[2]['label']}
Review: {test_review} | Sentiment:"""

print(f"Zero-shot: {get_model_response(zero_shot_prompt)}")
print(f"One-shot: {get_model_response(one_shot_prompt)}")
print(f"Few-shot: {get_model_response(few_shot_prompt)}")