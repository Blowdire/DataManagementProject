import requests
import time
import hashlib
API_PUBLIC_KEY = "929b4b43b3ab59b27417573fcd5868b9"
API_PRIVATE_KEY = "27bc1b826da0c2def3525f69a2668e7834744938"
API_LIMIT = 10
API_OFFSET = 0
current_timestamp = time.time()
hash = hashlib.md5((str(current_timestamp)+API_PRIVATE_KEY+API_PUBLIC_KEY).encode())
print('https://gateway.marvel.com:443/v1/public/characters?limit=100&apikey=929b4b43b3ab59b27417573fcd5868b9&hash='+hash.hexdigest())
response_API = requests.get('https://gateway.marvel.com:443/v1/public/characters?limit=%s&offset=%s&apikey=929b4b43b3ab59b27417573fcd5868b9&hash=%s&ts=%s'%(API_LIMIT,API_OFFSET,hash.hexdigest(),str(current_timestamp)))
with open("test_chiamata.json","w") as out_file:
  out_file.write(response_API.text)
