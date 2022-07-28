## Проект Система отзывов и оценок на произведения

### Сведения о проекте:

Проект **YaMDb** предназначен для сбора отзывов на произведения.
Произведения могут быть: *"Книги"*, *"Фильмы"*, *"Музыка"*. 

### Состав проекта:

Проект включает в себя:

1. Систему хранения и обработки информации по произведениям, отзывам и 
пользователям.
2. Систему удаленного доступа к информации, реализованную с помощью
REST архитектуры.

### Возможности проекта:

1. Проект позволяет хранить информацию:
    * о пользователях
    * о произведениях
    * об отзывах к произведениям и их комментариях
2. Проект позволяет указать дополнительную информацию о произведении:
    * жанр (фантастика, триллер и т.п.)
    * категория (фильм, книга, музыка и т.п.)
3. Проект позволяет работать с пользователями:
    * регистрировать пользователя
    * получать информацию о своем пользователе
    * получать параметры аутентификации для работы по API протоколу
4. Проект позволяет указать роль доступа пользователя:
    * пользователь
    * модератор
    * администратор
5. Проект позволяет добавлять отзывы к произведениям:
    * в отзыве выставляется оценка (от 1 до 10)
    * произведение имеет автоматически рассчитываемый рейтинг на 
основе оценок в отзывах

### Возможности API проекта:

1. Пользователи
    * добавление пользователя
    * получение параметров аутентификации
    * управление пользователями (удаление, изменение, просмотр)
2. Категории
    * добавление категорий
    * управление категориями (удаление, просмотр)
3. Жанры
    * добавление жанров
    * управление жанрами (удаление, просмотр)
4. Произведения
    * добавление произведений
    * управление произведениями (удаление, изменение, просмотр)
5. Отзывы к произведениям
    * добавление отзывов
    * управление отзывами (удаление, изменение, просмотр)
6. Комментарии к отзывам
    * добавление комментариев
    * управление комментариями (удаление, изменение, просмотр)

### Технические требования проекта

```
requests==2.26.0
django==2.2.16
djangorestframework==3.12.4
djangorestframework-simplejwt==5.1.0
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
django-filter==21.1
gunicorn==20.0.4
psycopg2-binary==2.9.2
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/web2cap/infra_sp2.git
```

```
cd infra_sp2/infra
```

#### Подготовка .env файла

Создайте файл переменных окружения в infra_sp2/infra
```
touch .ent
```
Заполните файл .env по шаблону:

```
ST_SECRET_KEY = "" # Django SECRET_KEY
DB_ENGINE=django.db.backends.postgresql_psycopg2 #Адаптер БД
DB_NAME= # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```


Запустить Docker-compose

```
docker-compose up -d --build 
```

Выполнить миграции, собрать статику:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input 
```

Можно создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Можно загрузить тестовые данные в базу данных:

```
docker-compose exec web python manage.py loaddata
```


### Описание API

Описание API методов проекта доступно по адресу: http://127.0.0.1/redoc/

### Автор:

* Кошелев Павел