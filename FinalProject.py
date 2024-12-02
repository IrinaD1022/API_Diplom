import requests
import configparser
import tqdm

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")
vk_token = config['Tokens']['vk_token']

class VK:
    def __init__(self, access_token, version='5.199'):
        self.base_address = 'https://api.vk.com/method/'
        self.params = {
            'access_token': access_token,
            'v': version
        }
    
vk = VK(vk_token, 'hirrrka')


    