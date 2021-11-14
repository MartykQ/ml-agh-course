import json
from typing import List

import requests
from googletrans import Translator

from server.sentiment_server.common.settings import IBM_TOKEN


def translate_to_eng(sentences: List[str]):
    translator = Translator()
    result = translator.translate(sentences, src='pl', dest='en')
    return result


def predict(sentences: List[str]):
    text_payload = ". ".join(sentences)

    url = "https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com" \
          "/instances/ce167fd3-9acd-4149-9a70-07dc113cc46e/v1/analyze?version=2021-08-01"

    headers = {
        'Authorization': f'Basic {IBM_TOKEN}',
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "text": text_payload,
        "features": {
            "sentiment": {
                "targets": sentences
            }
        }
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def translate_and_perdict(sentences: List[str]):
    results = []
    raw_translations = translate_to_eng(sentences)
    translations = [s.text for s in raw_translations]

    for sentence, translation in zip(sentences, translations):
        results.append({
            'text': sentence,
            'traslated': translation
        })

    predicitons = predict(translations)['sentiment']['targets']
    for result, prediction in zip(results, predicitons):
        result['label'] = prediction['label']
        result['score'] = prediction['score']

    return results
