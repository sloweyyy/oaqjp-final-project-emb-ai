# Emotion Detection API Project

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Testing](#testing)
7. [Directory Structure](#directory-structure)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview

This project is a Flask-based web application that provides an API for detecting emotions in text using IBM Watson's NLP service. The system analyzes the input text and returns the detected emotions (anger, disgust, fear, joy, sadness) along with the dominant emotion.

The frontend is a simple HTML page where users can input text and receive emotion analysis results dynamically.

---

## Features

- **Emotion Detection**: Analyzes text to detect emotions such as anger, disgust, fear, joy, and sadness.
- **Dominant Emotion Identification**: Identifies the most prominent emotion in the provided text.
- **Flask Backend**: Provides a RESTful API for emotion detection.
- **Frontend Interface**: A user-friendly interface to interact with the API.
- **Error Handling**: Handles invalid or empty input gracefully.

---

## Installation

### Prerequisites
- Python 3.6 or higher
- `pip` package manager
- IBM Watson NLP API access (credentials required)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/sloweyyy/oaqjp-final-project-emb-ai.git
   cd sloweyyy-oaqjp-final-project-emb-ai
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up IBM Watson credentials:
   - Replace the URL and headers in `EmotionDetection/emotion_detection.py` with your IBM Watson NLP API credentials.

5. Run the Flask server:
   ```bash
   python server.py
   ```

6. Open your browser and navigate to `http://localhost:5000` to access the application.

---

## Usage

1. Open the web interface at `http://localhost:5000`.
2. Enter the text you want to analyze in the input box.
3. Click the "Run Sentiment Analysis" button.
4. The results will be displayed below the button, showing the detected emotions and the dominant emotion.

---

## API Endpoints

### 1. GET `/`
- **Description**: Renders the home page (`index.html`).
- **Response**: HTML page with a form for text input.

### 2. POST `/emotionDetector`
- **Description**: Accepts a JSON payload with the key `"text"` and returns the emotion analysis.
- **Request Body**:
  ```json
  {
      "text": "I am so happy I am doing this."
  }
  ```
- **Response**:
  - Success (200 OK):
    ```json
    {
        "response": "For the given statement, the system response is 'anger': 0.1, 'disgust': 0.05, 'fear': 0.02, 'joy': 0.8, 'sadness': 0.03. The dominant emotion is joy."
    }
    ```
  - Error (400 Bad Request):
    ```json
    {
        "response": "Invalid text! Please try again!"
    }
    ```

---

## Testing

To run unit tests for the emotion detection module:

1. Ensure you have installed the required dependencies.
2. Run the following command:
   ```bash
   python -m unittest test_emotion_detection.py
   ```

The tests cover various scenarios, including:
- Text expressing joy
- Text expressing anger
- Text expressing disgust
- Text expressing sadness
- Text expressing fear

---

## Directory Structure

```
└── sloweyyy-oaqjp-final-project-emb-ai/
    ├── server.py                  # Flask server implementation
    ├── test_emotion_detection.py  # Unit tests for emotion detection
    ├── EmotionDetection/          # Emotion detection module
    │   ├── __init__.py            # Package initializer
    │   ├── emotion_detection.py   # Core logic for emotion detection
    │   └── __pycache__/           # Compiled Python files
    └── oaqjp-final-project-emb-ai/
        ├── .gitignore             # Git ignore file
        ├── static/                # Static files (JavaScript)
        │   └── mywebscript.js     # Frontend script for API interaction
        └── templates/             # HTML templates
            └── index.html         # Main HTML page
```

---

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature or fix"
   ```
4. Push your branch to GitHub:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
