import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        # Verify that the dominant emotion is 'joy'
        self.assertEqual(result.get('dominant_emotion'), 'joy')

    def test_anger(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        # Verify that the dominant emotion is 'anger'
        self.assertEqual(result.get('dominant_emotion'), 'anger')

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        # Verify that the dominant emotion is 'disgust'
        self.assertEqual(result.get('dominant_emotion'), 'disgust')

    def test_sadness(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        # Verify that the dominant emotion is 'sadness'
        self.assertEqual(result.get('dominant_emotion'), 'sadness')

    def test_fear(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        # Verify that the dominant emotion is 'fear'
        self.assertEqual(result.get('dominant_emotion'), 'fear')

if __name__ == '__main__':
    unittest.main()
