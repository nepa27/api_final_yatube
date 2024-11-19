# EasyBlog

Обучающий проект EasyBlog является прототипом сети для публикации постов,
подписки на интересных авторов и комментирования их 
записей.

Для проекта EasyBlog реализовано API на основе Django Rest Framework.
Аутентификация осуществляется с помощью токена JWT.

### Установка

Клонируйте репозиторий и перейдите в папку с проектом
```
git clone git@github.com:nepa27/easy_blog.git
cd easy_blog
```
Создайте **виртуальное окружение**
```
python3 -m venv venv
source venv/bin/activate    # (Ubuntu)
./venv/Scripts/python       # (Windows)
```
Затем установите необходимые зависимости из файла **requirements.txt**
```
pip install -r requirements.txt
```
Выполните миграции
```
python manage.py runserver
```

## Запуск

Перейдите в корневую директорию проекта, где находится файл **manage.py**
и запустите сервер
```
cd easy_blog
python3 manage.py runserver
```
Если вы все правильно сделали, то высветится приглашение
```
System check identified no issues (0 silenced).
April 20, 2024 - 15:35:58
Django version 3.2.16, using settings 'easy_blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Откройте браузер и перейдите по адресу **http://127.0.0.1:8000/redoc/**.
Здесь представлена документация для API EasyBlog. В документации описано, как должен работать ваш API.
Документация представлена в формате Redoc.


При возникновении ошибки
```
python: can't open file 'easy_blog/manage.py'[Errno 2] No such file or directory
```
убедитесь, что вы находитесь в корневой директории проекта

### Примеры запросов 
* Получение и создание постов: 
  ```
  http://127.0.0.1:8000/api/v1/posts/
  
  GET Request
  {
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
      {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-10-14T20:41:29.648Z",
        "image": "string",
        "group": 0
      }
    ]
  }
  
  POST Request
  Request:
  {
    "text": "string",
    "image": "string",
    "group": 0
  }
  Response:
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
  }
  ```
* Получение и создание нового комментария: 
  ```
  http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
  
  GET Request
  Response:
  [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "created": "2019-08-24T14:15:22Z",
      "post": 0
    }
  ]
  
  POST Request
  Request:
  {
    "text": "string"
  }
  Response:
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
  ```
* Получение JWT-токена:
  ```
  http://127.0.0.1:8000/api/v1/jwt/create/
  
  POST Request
  Request:
  {
    "username": "string",
    "password": "string"
  }
  Response:
  {
    "refresh": "string",
    "access": "string"
  }

  ```
  
### Инструменты и стек
#python #Django #DRF #Redoc #JWT

### Автор
Непочатых Александр
