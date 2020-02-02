import requests

class YandexTranslate():

    lang = input('Enter the language from which to translate : ')

    def translate_it(self, text, lang):

        API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

        params = {
            'key': API_KEY,
            'text': text,
            'lang': lang,
        }

        inquiry = requests.get(URL, params=params)
        json_ = inquiry.json()
        return ''.join(json_['text'])


