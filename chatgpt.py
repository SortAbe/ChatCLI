#!/bin/env python3

import os
import sys
import requests

message = sys.argv[1]
key = os.environ.get('GPT')
payload = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role':'user', 'content':message}],
        'temperature': 0.7
}

header = {
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer ' + key
}

response = requests.post('https://api.openai.com/v1/chat/completions', json=payload, headers=header)

print(response.json()['choices'][0]['message']['content'])
