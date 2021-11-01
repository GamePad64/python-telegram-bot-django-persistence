# python-telegram-bot-django-persistence
[![PyPI - Downloads](https://img.shields.io/pypi/dm/python-telegram-bot-django-persistence?style=for-the-badge)]()

Do you use [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) with Django
and want persistence without additional infrastructure? We've got you covered!

## Quickstart

### 📥 Install package
If you are using [poetry](https://python-poetry.org) (and if not, please, consider using it 😉):
```shell
poetry add python-telegram-bot-django-persistence
```

Elif you are using `pip`, then just enter:
```shell
pip install python-telegram-bot-django-persistence
```

### 🔌 Add the app to your Django project
Then add `python_telegram_bot_django_persistence` into your `INSTALLED_APPS` in your settings file, like so:

```python
INSTALLED_APPS = [
    ...
    "python_telegram_bot_django_persistence",
]
```

### ☢ Migrate your database
```shell
python manage migrate
```

### 🌟 Awesome! Use DjangoPersistence in python-telegram-bot
```python
updater = Updater(bot=bot, use_context=True, persistence=DjangoPersistence())
```
