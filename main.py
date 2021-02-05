import requests
import os

token = os.environ['token']


def getUpdates():
    url_up = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_u = requests.get(url=url_up)
    data = respons_u.json()['result']
    last_msg = data[-1]

    return last_msg



    

# url = 'https://ismlar.com/uz/name/%D0%94%D0%B8%D1%91%D1%80'

# r = requests.get(url)

# # print(r.text)

# idx1 = r.text.index('meta property="og:description" content="')
# mano = r.text[idx1+40:r.text.index('"', idx1+41)]

# print(mano)
