"""
Emotion Detection Server
This script initiates a Flask server for emotion detection processing.
It exposes an endpoint to analyze text and return the dominant emotion
along with the scores for anger, disgust, fear, joy, and sadness.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the sentiment of the provided text.
    Retrieves text from request arguments, passes it to the emotion detector,
    and returns a formatted string with the emotion scores and dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant emotion is None, indicating an error or invalid text
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract the emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Return a formatted string with the sentiment analysis results
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index page.
    This function handles the root route and displays the index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application on localhost:5000
    app.run(host="0.0.0.0", port=5000)