# Api_final_yatube

## О проекте
REST API для социальной сети yatube.
Позволяет производить действия с постами, комментариями, сообществами и подписками.

## Требования
- Python 3.7 
- Django 2.2.19
- Djangorestframework 3.16

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yoninjago/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
### Примеры использования
**Получение списка постов**
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/' --header 'Authorization: Bearer <your-token>'
[
    {
        "id": 1,
        "author": "user",
        "text": "New post",
        "pub_date": "2022-03-10T20:40:55.107802Z",
        "image": null,
        "group": 1
    },
    {
        "id": 7,
        "author": "dude",
        "text": "This is Dude",
        "pub_date": "2022-03-12T18:49:49.436966Z",
        "image": null,
        "group": 2
    }
]
```
**Создание поста**
```
$ curl --location --request POST 'http://127.0.0.1:8000/api/v1/posts/' \
--header 'Authorization: Bearer <your-token>' --header 'Content-Type: application/json' --data-raw '{"text": "This is Dude", "group": 2}'
{
    "id": 7,
    "author": "dude",
    "text": "This is Dude",
    "pub_date": "2022-03-12T18:49:49.436966Z",
    "image": null,
    "group": 2
}
```
### Лицензия
Этот проект лицензируется в соответствии с лицензией MIT — подробности см. в файле [LICENSE](https://github.com/yoninjago/yatube_project/blob/main/LICENSE).
