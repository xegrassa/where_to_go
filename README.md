# Куда пойти
Проект представляет карту Москвы с отмеченными на ней местами, интересными для посещения. По нажатию 
на интересующее место можно получить дополнительную информацию по нему.

## Тестовая версия сайта
У проекта существует страничка https://xegrassax.pythonanywhere.com/, размещённая с помощью сервиса 
[pythonanywhere.com](https://www.pythonanywhere.com). 

## Как установить

### Переменные окружения 
Создайте файл `.env` в корне:
```
DEBUG=False # Запуск в DEBUG режиме, для локального запуска True
SECRET_KEY=django-insecure-hh_fasfsdafuy^@fda1312 # Секретный ключ Django
ALLOWED_HOSTS=127.0.0.1,1.2.3.4 # Разрешенные хосты (по умолчанию 127.0.0.1)
```
### Запуск проекта
- Установлен [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- `python3 -m venv venv` установка виртуального окружения
- `python3 -m pip install -r requirements.txt` установка библиотек
- `python3 manage.py migrate` создание БД
- `python3 manage.py createsuperuser` создание суперпользователя для Админки
- `python3 manage.py runserver` запуск сервера

## Наполнение данными
Помимо добавления данных через Django-админку можно выполнить команду `python3 manage.py load_place`.
Команда загружает в БД данные из json файлов, ссылки на которые нужно указать при запуске.

### Пример json файла
```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

### Пример команд для загрузки данных

- Загрузка из файла `python3 manage.py load_place --file-path places_urls.txt` (в файле лежат пара мест)
- Загрузка по урле `python3 manage.py load_place --urls https://123.json https://qwe.json`
- Добавить вывод DEBUG сообщений `--verbose`
- Кол-во потоков для загрузки json, image `--thread-count 6` (по умолчанию 6)


## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).