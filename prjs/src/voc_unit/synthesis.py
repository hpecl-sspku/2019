from aip import AipSpeech
from playsound import playsound

def syn(text):
    #with open(r'F:\exploitation\codes\python\Spider\text\reading.txt', 'r', encoding='utf-8') as f:
    #content_s = f.read()
    APP_ID = '18142984'
    API_KEY = 'iVpZjZUWUUON4zV4bIkwrMb6'
    SECRET_KEY = 'Z0e3j3qUzO5Wom7qi0ZBrgETNvHWqBI1'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(text, 'zh', 1, {
    'vol': 5,
    'spd': 1,
    'pit': 7,
    'per': 4,
    })
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    playsound("auido.mp3")