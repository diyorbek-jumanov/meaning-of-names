import requests
import os

# token = os.environ['token']
token = '1616821732:AAHHPWF4mcOS8OACiCHTGnV1qRbUsBAqlN0'


def getUpdates():
    url_up = f'https://api.telegram.org/bot{token}/getUpdates'
    respons_u = requests.get(url=url_up)
    data = respons_u.json()['result']
    last_msg = data[-1]
    # print(last_msg)
    return last_msg


def Mean_name(text):
    
    url = f'https://ismlar.com/uz/search/{text}'
    r = requests.get(url)
    
    data = r.text
    # print(data)

    i_1 = data.find('<i class="fas fa-tag"></i>') + 59
    i_2 = data.find("\n", i_1)

    lang = data[i_1:i_2]
    # print(lang)
    i_3 = data.find('Сизнинг сўровингиз бўйича топилган натижалар сони:') + 56
    i_3 = data.find('-link"', i_3)
    if data[i_3-2] == 'y':
        category = "o'g'il bolalarning ismi"
    else:
        category = "qiz bolalarning ismi"
    i_3 = i_3 + 32
    # print(category)
    i_4 = data.find('\n', i_3)
    ism = data[i_3:i_4]
    # print(ism)
    i_5 = data.find('text-size-5', i_4) + 13
    i_6 = data.find('</p>', i_5)
    mano = data[i_5:i_6]
    # print(mano)

    ful_mano = f'{ism} - {lang}\n____________________\n{category}\n_____________________\n{mano}'
    # print(ful_mano)
    return ful_mano

    
def sendMsg(txt, ch):
    url_up = f'https://api.telegram.org/bot{token}/sendMessage'
    p = {
        'chat_id': ch,
        'text': txt
    }
    respons_s = requests.get(url=url_up, params=p)
    

msg_id = getUpdates()['message']['message_id']
while True:
    data = getUpdates()
    # print(data)
    last_msg_id = data['message']['message_id']
    chat_id = data['message']['from']['id']
    
    msg_text = data['message']['text']
    

    if msg_id != last_msg_id:

        sendMsg(Mean_name(msg_text), chat_id)
        msg_id = last_msg_id


