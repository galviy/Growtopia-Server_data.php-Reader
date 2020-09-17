import os
from os import system
import requests
import time
from time import sleep



os.system('cls')
print("Growtopia/server_data.php Reader (C)")
target = input('TARGET IP: ')

post = requests.post(f'http://{target}/growtopia/server_data.php')
print(post.text)
sleep(10)