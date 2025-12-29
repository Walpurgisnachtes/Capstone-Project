# Please install OpenAI SDK first: `pip3 install openai`
import os
import json
import secrets
from typing import List, Dict, Union, Callable, Any, Optional
from openai import OpenAI

import configparser

def get_api_key(config_file):
    config = configparser.ConfigParser()

    if not os.path.exists(config_file):
        print(f"Error: {config_file} not found.")
        return None

    config.read(config_file)

    try:
        api_key = config['API']['API_KEY']
        return api_key
    except KeyError as e:
        print(f"Error: Missing section or key in config: {e}")
        return None

# Usage
if __name__ == '__main__':
    api_key = get_api_key(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/backend/config.ini")

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)