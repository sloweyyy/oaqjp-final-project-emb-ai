import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    data = json.loads(response.text)
    
    emotions = data.get('emotion', {}).get('document', {}).get('emotion', {})
    anger_score   = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score    = emotions.get('fear', 0)
    joy_score     = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion
    
    return result

if __name__ == '__main__':
    sample_text = "I am so happy I am doing this."
    output = emotion_detector(sample_text)
    print("Formatted Emotion Output:")
    print(json.dumps(output, indent=4))
