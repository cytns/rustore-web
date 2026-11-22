# RuStore Web

Простая витрина популярных приложений RuStore.

Пользователь может:

- посмотреть список из 50 приложений
- увидеть категорию и рейтинг приложения
- перейти на страницу приложения в RuStore

## Стек

Frontend:

- HTML
- CSS

Backend:

- Python
- Flask
- Gunicorn

БД:

- SQLite

## Запуск проекта

Создать виртуальное окружение:

```bash
python3 -m venv .venv
```

Активировать окружение:

```bash
source .venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить приложение:

```bash
python app.py
```

Открыть в браузере: http://127.0.0.1:5000/

## Запуск тестов

```bash
python -m unittest -v
```

## Попробовать онлайн

https://rustore-web.onrender.com/