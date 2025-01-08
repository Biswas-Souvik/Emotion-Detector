import json
import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_body = { "raw_document": { "text": text_to_analyze } }

    resp = requests.post(url, json = req_body, headers = headers)
    if resp.status_code == 400:
        emotions_scores = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    else:

        resp_json = json.loads(resp.text)
        emotions_scores = resp_json["emotionPredictions"][0]["emotion"]
        
        dominant_emotion = None
        dominant_score = 0
        
        for emotion in emotions_scores:
            if emotions_scores[emotion] > dominant_score:
                dominant_score = emotions_scores[emotion]
                dominant_emotion = emotion

        emotions_scores["dominant_emotion"] = dominant_emotion

    return emotions_scores
