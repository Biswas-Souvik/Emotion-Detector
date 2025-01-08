"""The Flask app file"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_page():
    """Function to provide the emotion"""

    text_to_analyse = request.args.get("textToAnalyze")
    emotion_dict = emotion_detector(text_to_analyse)
    if emotion_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    resp = f"""For the given statement, the system response is
    'anger': {emotion_dict['anger']}, 'disgust': {emotion_dict['disgust']}, 
    'fear': {emotion_dict['fear']}, 'joy': {emotion_dict['joy']} and 
    'sadness': {emotion_dict['sadness']}. 
    The dominant emotion is {emotion_dict["dominant_emotion"]}."""

    return resp


@app.route("/")
def home():
    """Function to display the home page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
