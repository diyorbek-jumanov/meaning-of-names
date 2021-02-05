import requests
url = 'https://ismlar.com/uz/name/%D0%94%D0%B8%D1%91%D1%80'

r = requests.get(url)

print(r.text)
