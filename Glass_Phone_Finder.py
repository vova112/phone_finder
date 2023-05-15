import requests
from bs4 import BeautifulSoup

phone_name = input("Введите название телефона: ")

notch = input("У смартфона фронталка капелькой(1) или отверстием(2)? [1/2]: ")
if notch == '1':
	notch = 2
else:
	notch = 3
url = f"https://specificationsplus.com/en/{phone_name.lower().replace(' ', '-')}/"

curved = input("Экран изогнутый? [y/n]: ")
if curved == 'y':
	curved = 1
else:
	curved = 0

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

dimensions = soup.find_all("span", class_="aps-1co")
if len(dimensions) > 1:
    dimensions = dimensions[9].text.strip()
    #print (dimensions)

else:
    print("Не удалось найти размеры телефона.")
try:
    size_mm = dimensions.split(' ')
    visota_0 = size_mm[0].replace(',','.')
    shirina_0 = size_mm[2].replace(',','.')
    visota_1 = float(visota_0)-1
    visota_2 = float(visota_0)+1
    shirina_1 = float(shirina_0)-1
    shirina_2 = float(shirina_0)+1
except:
    dimensions = soup.find_all("span", class_="aps-1co")
    if len(dimensions) > 1:
        dimensions = dimensions[8].text.strip()
        print(dimensions)
    size_mm = dimensions.split(' ')
    visota_0 = size_mm[0].replace(',', '.')
    shirina_0 = size_mm[2].replace(',', '.')
    visota_1 = float(visota_0) - 1
    visota_2 = float(visota_0) + 1
    shirina_1 = float(shirina_0) - 1
    shirina_2 = float(shirina_0) + 1

print('==============================================================')
print(f"Размеры {phone_name}: Высота - {visota_0}, Ширина - {shirina_0}")

url_2 = f"https://www.gsmarena.com/results.php3?nHeightMin={visota_1}&nHeightMax={visota_2}&nWidthMin={shirina_1}&nWidthMax={shirina_2}&idDisplayNotch={notch}"

response_2 = requests.get(url_2)
soup_2 = BeautifulSoup(response_2.content, "html.parser")

#models = soup_2.select('div.name a')
models = soup_2.find_all('strong')
print('==============================================================')
print(f'Модели тефонов, которые могут быть совместимы с {phone_name}. Инфа с GSMArena: ')
for model in models[:15]:
    print(model.text)
print('==============================================================')
print('Подождите...')
print('==============================================================')

url_3 = f"https://mobihobby.ru/phone/1?f_scr_curved={curved}&f_app_length[0]={visota_1}&f_app_length[1]={visota_2}&f_app_width[0]={shirina_1}&f_app_width[1]={shirina_2}"
response_3 = requests.get(url_3)
soup_3 = BeautifulSoup(response_3.content, "html.parser")
models_2 = soup_3.select('div.name a')
print(f'Модели тефонов, которые могут быть совместимы с {phone_name}. Инфа с MobbyHonbby: ')
for model_2 in models_2[:8]:
    print(model_2.text)

print('==============================================================')
wait = input('Нажми Enter чтобы выйти')
