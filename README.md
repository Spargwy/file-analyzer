#Анализатор текстовых файлов

Сервис принимает на вход текстовый файл, читает его содержимое и отдает TF-IDF 
слов, которые в нём содержатся.

##Стек
- Python/Django
- PostgreSQL
- Docker/Docker-compose

Приложение использует переменные окружения. Перед использованием необходимо создать 
файл .env в директории web_service/web_service и вписать туда следующее:
```
DB_PORT='5432'
DB_HOST='db'
```
Подставив при необходимости свои значения

В случае ручного запуска, требуется установка зависимостей командой

```pip install requirements.txt```

А также установка и накат миграций командами
```
python manage.py makemigrations
python manage.py migrate
```

После этого запуск осуществляется командой

```python manage.py runserver```

При запуске с помощью докера, необходимо сначала создать файл .env в директории web_service
с содержимым:
```
DB_USER_IN_DOCKER='postgres'
DB_IN_DOCKER='db'
DB_PASSWORD_IN_DOCKER='postgres'
DB_PORT_IN_DOCKER='5432:5432'
APP_PORT_IN_DOCKER='8900:8900'
RUN_PORT_IN_DOCKER='0.0.0.0:8900'
```
Содержимое также меняется на ваше усмотрение

С помощью докера, сервис можно запустить командой
```make docker-run```
