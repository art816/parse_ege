import requests
from bs4 import BeautifulSoup

s = requests.Session()
cookies = {'cookieEgeLevel' : '2'}
r = s.get('http://mathege.ru/or/ege/ShowProblems', cookies=cookies)
soup = BeautifulSoup(r.content, 'html.parser')
number_pages_text = soup.findAll(text=re.compile("Просмотр выбранных заданий с"))
start_task, last_task = list(map(int, re.findall('\d+', number_pages_text[0])))
last_task = 12
while start_task < last_task:
    r = s.get(
        'http://mathege.ru/or/ege/ShowProblems?offsetStr={}'.format(start_task),
        cookies=cookies)
    soup = BeautifulSoup(r.content, 'html.parser')


#print(soup.findAll(id="QuizBody"))
    quizbody = soup.find(id="QuizBody")
    task_number = 0
    while quizbody:
#print(td)
        table = quizbody.findParent('table')
        prototype = table.find(text=re.compile("Прототип")).findNext('td').find('a').text
        type_number_task_text = table.findPrevious('table').find('h2').text
        type_task, number_task = list(
            map(int, re.findall('\d+', type_number_task_text)))
        print(task_number, start_task, type_task, number_task)
        quizbody = quizbody.findNext(id="QuizBody")
        task_number += 1

    start_task += 5
#from matplotlib.pyplot import imshow, show
#from PIL import Image
#import shutil
#import io
#with open('my_file', 'wb') as f:
#    r.raw.decode_content = True
#    shutil.copyfileobj(io.BytesIO(r.content), f)
#imshow(Image.open('my_file'))
#imshow(Image.open(io.BytesIO(r.content)))
#show()
