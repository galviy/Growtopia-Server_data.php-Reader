import os
from os import system
import requests

os.system('clear')
print("Coded by GalvinID and KIPAS")
target = input('TARGET IP: ')

post = requests.post(f'http://{target}/growtopia/server_data.php')
print(post.text)