## Оглавление
- [Описание](#description)
- [Установка](#setup)
- [Примеры запросов через API](#examples)

<a id=description></a>
## Описание
Yatube API - проект, выполненый с использованием библиотеки [Django REST Framework](https://www.django-rest-framework.org/) фреймворка [Django](https://www.djangoproject.com/). В проекте реализованы приложения posts и api. Приложение posts позволяет пользователям публиковать статьи в предложенных им группах, комментировать статьи других пользователей, создавать подписки на других пользователей. Приложение api служит для обмена между клиентами пользователей и сервером посредством интерфейса API. Приложение непременно нужно тем, кому захотелось что-нибудь написать или почитать, вступить в группу единомышленников, обсудить чьи-то статьи. Проект api_final_yatube предоставляет широкие возможности для такого рода деятельности. :upside_down_face:

---
<a id=setup></a>
## Установка
Для установки проекта Вам необходимо его установить с помощью утилиты Git. С помощью консоли перейдите в папку, в которую будет установлен проект: `cd <папка_назначения>`. После этого клонируйте проект в папку назначения:
```
git clone https://github.com/I-Iub/api_final_yatube.git
```
Дождитесь сообщения о том, что проект успешно клонирован и перейдите в папку проекта:
```
cd api_final_yatube/
```
Разверните виртуальное окружение:
```
python -m venv venv
```
Активируйте виртуальное окружение:
```
source venv/Scripts/activate    # Windows
source venv/bin/activate        # Linux
```
Обновите pip и установите зависимости:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Создайте файл миграций и выполните миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Создайте файл ".env" в папке "api_final_yatube/yatube_api/yatube_api/". В файле укажите секретный ключ проекта: `SECRET_KEY = <секретный_ключ>`.
Запустите проект:
```
python manage.py runserver
```
---
<a id=examples></a>
## Примеры запросов через API
##### GET-запрос на получение списка публикаций
Запрос могут выполнять авторизованные и неавторизованные пользователи. Чтобы получить все публикации, необходимо выполнить GET-запрос к эндпоинту:
```
http://127.0.0.1:8000/api/v1/posts/
```
Пример ответа:
```
[
    {
        "id": 1,
        "author": "user1",
        "text": "Первый пост.",
        "pub_date": "2021-07-24T11:22:09.545328Z",
        "image": null,
        "group": null
    },
    ...
    {
        "id": 6,
        "author": "user4",
        "text": "Шестой пост(последний по порядку в этом примере).",
        "pub_date": "2021-07-24T14:20:42.296969Z",
        "image": null,
        "group": 3
    }
]
```

##### GET-запрос на получение списка публикаций с пагинацией
Также доступна пагинация. Можно в запросе указывать количество публикаций, которые должны выводится на страницу - параметр `limit`. А также указывать параметр `offset`. Публикации будут выводится на страницу начиная со следующего по порядку номеру после номера, переданного в параметре `offset`. Например, чтобы получить два поста на странице, начиная с четвертого (`offset=3`), необходимо выполнить GET-запрос к эндпоинту:
```
http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=3
```
Пример ответа:
```
{
    "count": 6,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=5",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=1",
    "results": [
        {
            "id": 4,
            "author": "user1",
            "text": "Text.",
            "pub_date": "2021-07-24T14:20:31.043377Z",
            "image": null,
            "group": null
        },
        {
            "id": 5,
            "author": "user2",
            "text": "Текст.",
            "pub_date": "2021-07-24T14:20:38.506475Z",
            "image": null,
            "group": 2
        }
    ]
}
```
Примеры других запросов и ответов можно посмотреть в браузере. Для этого при запущенном приложении необходимо ввести в строку браузера `http://127.0.0.1:8000/redoc/`.
