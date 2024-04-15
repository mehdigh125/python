import dotenv
import os
import requests
dotenv = dotenv.load_dotenv()
githubkey = os.getenv("githubkey") 
username = input("Please enter your username:")
url = "https://api.github.com/users/"+username
headers = {"Authorization": f"token {githubkey}"}        
response = requests.get(url, headers=headers) 
data = response.json()     
followers_count = data['followers']
following_count = data['following']
print(f"user={username} followers={followers_count} * following={following_count }")

