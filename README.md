# python-telegram-bot-django-persistence
[![PyPI - Downloads](https://img.shields.io/pypi/dm/python-telegram-bot-django-persistence?style=flat-square)](https://pypi.org/project/python-telegram-bot-django-persistence/)
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Do you use [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) or [aiogram](https://github.com/aiogram/aiogram) with Django
and want storing FSM info without additional infrastructure?  
We've got you covered!

Originally, this package supported only PTB, but we added aiogram, because it is awesome!

## Quickstart

### 📥 Install package
If you are using [poetry](https://python-poetry.org) (and if not, please, consider using it 😉):
```shell
# For python-telegram-bot
poetry add "python-telegram-bot-django-persistence[ptb]"
# For aiogram
poetry add "python-telegram-bot-django-persistence[aiogram]"
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
    "python_telegram_bot_django_persistence",  # For python-telegram-bot
    "aiogram_djpersistence",  # For aiogram
]
```

### ☢ Migrate your database
```shell
python manage migrate
```

### 🌟 Awesome! Now use it in your bot!

#### python-telegram-bot
```python
updater = Updater(bot=bot, use_context=True, persistence=DjangoPersistence())
```
#### aiogram
```python
dp = Dispatcher(storage=DjangoStorage())
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://shishenko.com"><img src="https://avatars.githubusercontent.com/u/837953?v=4?s=100" width="100px;" alt="Alexander Shishenko"/><br /><sub><b>Alexander Shishenko</b></sub></a><br /><a href="https://github.com/GamePad64/python-telegram-bot-django-persistence/commits?author=GamePad64" title="Code">💻</a> <a href="https://github.com/GamePad64/python-telegram-bot-django-persistence/commits?author=GamePad64" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rhutkovich"><img src="https://avatars.githubusercontent.com/u/9265526?v=4?s=100" width="100px;" alt="Raman Hutkovich"/><br /><sub><b>Raman Hutkovich</b></sub></a><br /><a href="https://github.com/GamePad64/python-telegram-bot-django-persistence/commits?author=rhutkovich" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
