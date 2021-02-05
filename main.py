import requests
import os

# token = os.environ['token']
token = '1529375049:AAGsVK_oy8Bs_mkcZitgGSs63GBH46ErUas'


def getUpdates():
    url_up = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_u = requests.get(url=url_up)
    data = respons_u.json()['result']
    last_msg = data[-1]
    # print(last_msg)
    return last_msg


def Mean_name(text):
    
    url = f'https://ismlar.com/uz/search/{text.title()}'
    r = requests.get(url)
    
    data = r.text

    i_1 = data.find('<i class="fas fa-tag"></i>') + 28
    i_2 = data.find("\n", i_1)

    lang = data[i_1:i_2]
    print(lang)
    i_3 = data.find('<p class="text-size-5">') + 24
    i_4 = data.find('</p>', i_3)
    mano = data[i_3:i_4]
    print(mano)
    # idx1 = data.find()
Mean_name("Faxriddin")
# Mean_name(msg_text)

# msg_id = 0
# while True:
#     data = getUpdates()
#     last_msg_id = data['message']['message_id']
#     chat_id = data['message']['from']['id']
#     msg_text = data['message']['text']

#     if msg_id != last_msg_id:
        
#         msg_id = last_msg_id


