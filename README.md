# Описание проекта

Api для проекта yatabe в котором можно изменять, добавлять и удалять посты.

# Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:D4rkLght/api_final_yatube.git
```
```
cd kittygram2
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
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
