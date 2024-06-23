import random
import asyncio
from pyrogram import Client, filters
import re
import os

# Задайте API ID и API Hash, полученные от Telegram
api_id = "api_id"
api_hash = "api_hash"

# Создайте клиент для взаимодействия с Telegram API
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Функция для сохранения комментариев из обсуждения
async def save_comments(channel_link, message_id):
    comments = []
    try:
        # Асинхронный цикл для получения ответов на сообщение
        async for message in app.get_discussion_replies(channel_link, message_id):
            # Получите имя пользователя, если оно доступно, иначе используйте "Anonymous"
            user_name = message.from_user.username if message.from_user else "Anonymous"
            # Сформируйте строку комментария
            comment = f"{user_name}: {message.text}\n"
            # Вставьте комментарий в начало списка для сохранения порядка
            comments.insert(0, comment)
    except Exception as e:
        # Обработайте исключения и выведите ошибку
        print(f"Failed to fetch comments: {e}")
        return

    # Если комментарии были получены
    if comments:
        # Укажите путь к файлу для сохранения комментариев
        file_path = os.path.join("/home/your_login/tg_comments", "tg_comments.txt")
        with open(file_path, "w") as file:
            # Запишите комментарии в файл
            file.writelines(comments)
        # Подготовьтесь к отправке файла с комментариями
        await prepare_to_send(file_path)

# Функция для подготовки к отправке файла с комментариями
async def prepare_to_send(file_path):
    # Отправьте команду для очистки предыдущих данных в чат GPT-бота
    await app.send_message("Your_GPT_Bot", "/clear")
    # Сделайте паузу, чтобы дать боту время на обработку
    await asyncio.sleep(random.randint(2, 4))
    # Отправьте файл с комментариями в чат
    await send_comments_to_chat(file_path)

# Функция для отправки файла с комментариями в чат
async def send_comments_to_chat(file_path):
    # Задайте подпись к документу
    caption = "Я хочу изучить комментарии к публикации. Проанализируй их и выведи очень кратко основные тезисы о чём общаются комментаторы."
    # Отправьте документ в чат с указанной подписью
    await app.send_document("Your_GPT_Bot", file_path, caption=caption)

# Обработчик сообщений, содержащих ссылки на сообщения в Telegram
@app.on_message(filters.chat("me") & filters.regex(r"https?://t\.me/(c/)?(\d+|\w+)/(\d+)"))
async def handle_link(client, message):
    # Используйте регулярное выражение для извлечения данных из ссылки
    url_match = re.search(r"https?://t\.me/(c/)?(\d+|\w+)/(\d+)", message.text)
    if url_match:
        # Извлеките префикс, ссылку на канал и ID сообщения
        prefix, channel_link, message_id = url_match.groups()
        if prefix:
            # Если есть префикс, добавьте его к ссылке на канал
            channel_link = f"-100{channel_link}"
        print(f"Handling link: channel_link={channel_link}, message_id={message_id}")
        
        # Убедитесь, что личный аккаунт знает чат
        try:
            await app.get_chat(channel_link)
        except Exception as e:
            # Обработайте исключения и выведите ошибку
            print(f"Failed to get chat: {e}")
            return
        
        # Сохраните комментарии к сообщению
        await save_comments(channel_link, int(message_id))

# Запустите клиента
app.run()
