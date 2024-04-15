import argparse
import requests
import json
import dotenv
import os

parser1 = argparse.ArgumentParser()
parser1.add_argument('name', help='enter your favorite flower?')
args = parser1.parse_args()
print(f'{args.name}')


dotenv=dotenv.load_dotenv()

diff_api=os.getenv("diff_api")
url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
payload = {
    "image_url":""https://github.com/mehdigh125/Python/blob/main/Assignment-02/image/pattern.png?raw=true"",
    #"image_url":"./image/pattern.png",
    "prompt": "(masterpiece:1.4), (best quality), (detailed), landscape,"+args.name,
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
}
# Status Code 401 - Unauthorized
headers = {
    "Authorization":diff_api ,
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
response.status_code
#response.json()
print(response.status_code)
print(response.text)
