import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    result = response.json()
    emotions = result.get("emotion_predictions", [{}])[0]

    emotion_scores = {
        'anger': emotions.get("anger", 0),
        'disgust': emotions.get("disgust", 0),
        'fear': emotions.get("fear", 0),
        'joy': emotions.get("joy", 0),
        'sadness': emotions.get("sadness", 0),
    }

    emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)

    return emotion_scores

if __name__ == '__main__':
    sample_text = "I am so happy I am doing this."
    output = emotion_detector(sample_text)
    print("Formatted Emotion Output:")
    print(json.dumps(output, indent=4))
