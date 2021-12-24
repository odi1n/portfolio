# Portfolio Generate

## Install, run project
1. Склонировать проект: `git clone git@github.com:odi1n/portfolio_generate.git`
2. Перейти в директорию: `cd portfolio_generate`
3. Изменить файл  `.env.example` на `.env`
4. Установить poetry: `pip install poetry`
5. Установить зависимости: `poetry install
6. Произвести миграцию: `python manage.py makemigrations`
7. Мигрировать: `python manage.py migrate`
8. Запустить: `python manage.py runserver`

## Run Docker
1. Склонировать проект: `git clone git@github.com:odi1n/portfolio_generate.git`
2. Перейти в директорию: `cd portfolio_generate`
3. Изменить файл  `.env.example` на `.env`
4. Запустить докер: `docker-compose up`
5. Произвести миграцию: `python manage.py makemigrations`
6. Мигрировать: `python manage.py migrate`

Добавить к образу докера в файле docker-compose-*.yml опцию user, в которой указать UID и GID пользователя, от которого будет запускаться докер контейнер:
```
user: "3203:3203" # 3203 - user id / group id пользователя в системе
```
