import requests
import json

def sentiment(review):

    files = {
        'text': (None, '%s' % review),
        'api_key': (None, 'SXiVV3pSbQodFZrTKytisrfihbCr9RWBEryJLMfYIOI'),
    }

    response = requests.post('https://apis.paralleldots.com/v4/sentiment', files=files)

    print(response.json())
    f = open("response.json", "w")
    f.write(json.dumps(response.json(), indent=4))
    f.close()
