"""
Flask Server for Emotion Detection API
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page (index.html).
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handles emotion detection API.
    - Accepts a JSON request with 'text' key.
    - Returns the emotion analysis in JSON format.
    - If text is empty, returns an error message.
    """
    data = request.json
    text_to_analyze = data.get("text", "")

    emotion_result = emotion_detector(text_to_analyze)

    if emotion_result["dominant_emotion"] is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    response_text = (f"For the given statement, the system response is "
                     f"'anger': {emotion_result['anger']}, "
                     f"'disgust': {emotion_result['disgust']}, "
                     f"'fear': {emotion_result['fear']}, "
                     f"'joy': {emotion_result['joy']} and "
                     f"'sadness': {emotion_result['sadness']}. "
                     f"The dominant emotion is {emotion_result['dominant_emotion']}.")

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
