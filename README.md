# python-telegram-bot-django-persistence
[![PyPI - Downloads](https://img.shields.io/pypi/dm/python-telegram-bot-django-persistence?style=flat-square)](https://pypi.org/project/python-telegram-bot-django-persistence/)
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://shishenko.com"><img src="https://avatars.githubusercontent.com/u/837953?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexander Shishenko</b></sub></a><br /><a href="https://github.com/GamePad64/python-telegram-bot-django-persistence/commits?author=GamePad64" title="Code">💻</a> <a href="https://github.com/GamePad64/python-telegram-bot-django-persistence/commits?author=GamePad64" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!