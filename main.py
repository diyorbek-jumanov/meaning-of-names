import requests
import os

# token = os.environ['token']
token = '1529375049:AAGsVK_oy8Bs_mkcZitgGSs63GBH46ErUas'


def getUpdates():
    url_up = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_u = requests.get(url=url_up)
    data = respons_u.json()['result']
    last_msg = data[-1]

    return last_msg


def Mean_name(text):
    url = f'https://ismlar.com/uz/search/{text}'
    r = requests.get(url)

    # idx1 = r.text.index('meta property="og:description" content="')
    ism = r.text[r.text.find(text):r.text.find(' ', r.text.find(text))]
    lang = r.text[r.text.find('<i class="fas fa-tag"></i>', r.text.find(text))+59:r.text.find('\n', r.text.find('<i class="fas fa-tag"></i>')+30)]
    mano = r.text[r.text.find('<p class="text-size-5">', r.text.find(text))+23:r.text.find('</p>', r.text.find('<p class="text-size-5">')+28)]
    print(r.text)
    print(ism)
    print(lang)
    print(mano)
    # print(r.url)
    return mano


msg_id = getUpdates()['message']['message_id']
while True:
    data = getUpdates()
    last_msg_id = data['message']['message_id']
    chat_id = data['message']['from']['id']
    msg_text = data['message']['text']

    if msg_id != last_msg_id:
        mean = Mean_name(msg_text)
        msg_id = last_msg_id


