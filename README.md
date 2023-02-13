# Portfolio Generate

## Install, run project

1. Склонировать проект: `git clone git@github.com:odi1n/portfolio_generate.git`
2. Перейти в директорию: `cd portfolio_generate`
3. Изменить файл  `.env.example` на `.env`
4. Установить poetry: `pip install poetry`
5. Установить зависимости: `poetry install`
6. Произвести миграцию: `python manage.py makemigrations`
7. Мигрировать: `python manage.py migrate`
8. Запустить: `python manage.py runserver`

## Run Docker
1. Склонировать проект: `git clone git@github.com:odi1n/portfolio_generate.git`
2. Перейти в директорию: `cd portfolio_generate`
3. Изменить файл  `.env.example` на `.env`
4. Собрать докер: `docker-compose build`
5. Запустить докер: `docker-compose up`
6. Создать пользователя: `docker exec -it pr_web python manage.py createsuperuser`

## Run Docker Prod

1. Склонировать проект: `git clone git@github.com:odi1n/portfolio_generate.git`
2. Перейти в директорию: `cd portfolio_generate`
3. Изменить файл  `.env.example` на `.env`
4. Собрать докер: `docker-compose -f docker-compose-prod.yml build`
5. Запустить докер: `docker-compose -f docker-compose-prod.yml up`
