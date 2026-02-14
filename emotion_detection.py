import requests

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the dictionary with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=headers)
    
    # Return the text attribute of the response object
    return response.text
