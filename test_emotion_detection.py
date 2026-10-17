from emotion_detection import emotion_detector

def test_emotion_detector():
    result = emotion_detector("I am really mad about this")
    assert result is not None
    assert len(result) > 0

if __name__ == "__main__":
    test_emotion_detector()
    print("Emotion detector test passed!")
