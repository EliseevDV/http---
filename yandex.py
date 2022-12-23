import requests
from pprint import pprint
# response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
# data = response.json()
# heroes = []
# for hero in data:
#     if hero["name"] in ('Hulk', 'Captain America', 'Thanos'):
#         heroes.append(hero)
# heroes.sort(key=lambda hero: hero['powerstats']['intelligence'], reverse=True)
#
# pprint(heroes[0])

class YaUploader:
    def __init__(self, token: str, url:str):
        self.token = token
        self.url = url

    def upload(self, file_path: str, savefile:str, headers, replace = False):

        res = requests.get(f'{self.url}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)

        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r'C:\Users\A590\Desktop\DZ_Read\recipes.txt'
    token = ''
    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': f'OAuth {token}'}
    requests.put(f'{url}?path=api1', headers=headers)

    uploader = YaUploader(token, url)
    uploader.upload(path_to_file, 'api1/resipt.txt', headers)