
# Мониторинг визовых слотов (Calgary)

## Что нужно:

1. Создай Telegram-бота через @BotFather, скопируй токен.
2. Напиши своему боту `/start`, получи `chat_id` (или через curl).
3. Экспортируй HAR с сайта https://ais.usvisa-info.com после входа в аккаунт.
4. Назови его `cookies.json` и положи в корень проекта.

## Как развернуть:

### Railway (1 минута):

1. Зайди на https://railway.app
2. Нажми "New Project" → "Deploy from GitHub" или "Deploy from Template"
3. Залей ZIP из этого архива (или GitHub-репозиторий)
4. В разделе Variables добавь:

- `TG_BOT_TOKEN` — токен из @BotFather
- `TG_CHAT_ID` — свой Telegram chat_id

5. Зайди во вкладку Deploy → "Start deployment"
6. Всё! Бот будет проверять слоты каждые 5 минут

Если что — пиши `/start` своему боту, он ответит.
