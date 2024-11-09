import requests
from bs4 import BeautifulSoup




url = 'https://habr.com/ru/post/453444/'
get = requests.get(url=url)
soup = BeautifulSoup(get.text, 'html.parser')#нормальный вид html + find_all




#список с именами проектов
soup_name = soup.find_all('b')#'b' - tag name, soup_name - список, но заполненный не str() типами данных

names_of_projects = []
for i in range(len(soup_name)):
    a = soup_name[i].text
    if i == 0:
        a = a.replace('1. ', '')#кривая запись первого имени в самой статье
        names_of_projects.append(a)
    else:
        names_of_projects.append(a)



#список с именами на github
soup_reference = soup.find_all('a')

names_on_git = []
for i in range(len(soup_reference)):
    a = soup_reference[i].text
    if 'github.com' in a:
        a = a.split('/')[-1]#конец ссылки --> username in GitHub
        names_on_git.append(a)





#словарь {'имя проекта': 'имя на GitHub'}
final_dict = {}
for i in range(100):
    final_dict[names_of_projects[i]] = names_on_git[i]


with open('list_txt', '+w') as file:
    file.write(f'{str(final_dict)}\n{str(names_on_git)}')