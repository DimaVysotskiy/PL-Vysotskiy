import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/post/453444/'
get = requests.get(url=url)

soup = BeautifulSoup(get.text, 'html.parser')



#список с именами репозиториев
soup_name = soup.find_all('b')

list_with_name_of_repository = []
for i in range(len(soup_name)):
    a = soup_name[i].text
    if i == 0:
        a = a.replace('1. ', '')#кривая запись первого имени в самой статье
        list_with_name_of_repository.append(a)
    else:
        list_with_name_of_repository.append(a)



#список с именами на github
soup_reference = soup.find_all('a')

name = []
for i in range(len(soup_reference)):
    a = soup_reference[i].text
    if 'github.com' in a:
        a = a.split('/')[-1]
        name.append(a)






#словарь имя --> ссылка
final_dict = {}
for i in range(100):
    final_dict[list_with_name_of_repository[i]] = name[i]


with open('list_txt', '+w') as file:
    file.write(f'{str(final_dict)}\n{str(name)}')